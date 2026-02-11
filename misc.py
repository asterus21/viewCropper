'''
The module contains miscellaneous functions, i.e. those which
- print the current time
- close the script
- process the user's input
- get a list of target pixels
- find target pixels for views
- find target pixels for wizards
'''

import datetime
import os
import sys
from pathlib import Path


def print_time() -> str:
    '''Prints the current time.'''
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_time


def close_script() -> None:
    '''closes the script'''
    # add an empty line before the closing statetement
    print()
    input('Press Enter to close the program.')

    sys.exit(0)


def process_input(user_input: str) -> str:
    '''validates the user's input'''
    p = Path(user_input)
    # the entered path must exist and be a folder
    if not p.exists() and not p.is_dir():
        print('No valid path is provided.')
        input('Press Enter to close to programm.')
        sys.exit(1)    
    else:
        return user_input


def get_targets(image, x: int, y: int) -> dict:
    '''finds target pixels and their neighbours'''
    targets = dict(
        target = image.getpixel((x, y)),
        right  = image.getpixel((x + 1, y)),
        down   = image.getpixel((x, y + 1)),
        left   = image.getpixel((x - 1, y)),
        up     = image.getpixel((x, y - 1))
    )
    return targets


def find_targets_in_view(image, height, width, central, right, left):
    '''creates of list of target pixels for views'''
    coordinates = []
    for x in range(width - 1):
        for y in range(height - 1):
            t = get_targets(image, x, y)
            if (
                (
                    t.get('target') == central[0] or
                    t.get('target') == central[1] or
                    t.get('target') == central[2] or
                    t.get('target') == central[3]
                ) and
                (
                    t.get('right')   == right[0] or 
                    t.get('right')   == right[1] or
                    t.get('right')   == right[2]
                ) and
                (
                    t.get('left')    == left[0] or 
                    t.get('left')    == left[1] or
                    t.get('left')    == left[2]
                )
            ): coordinates.append((x, y))
    return coordinates


def find_targets_in_wizard(image, height, width, upper, upper_neighbor, lower, lower_neighbor):
    '''creates a list of target pixels for wizards'''
    target_left_coordinates  = []
    target_right_coordinates = []
    for x in range(width - 1):
        for y in range(height - 1):
            t = get_targets(image, x, y)
            if (
                    (
                    t.get('target') == upper[0] or 
                    t.get('target') == upper[1] or 
                    t.get('target') == upper[2] or 
                    t.get('target') == upper[4] or 
                    t.get('target') == upper[5] or 
                    t.get('target') == upper[6] or
                    t.get('target') == upper[7]
                    ) and 
                    (
                    t.get('right')  == upper_neighbor[0] or 
                    t.get('right')  == upper_neighbor[1] or 
                    t.get('right')  == upper_neighbor[2]
                    )
                    and 
                    (
                    t.get('down')   == upper_neighbor[0] or
                    t.get('down')   == upper_neighbor[1] or  
                    t.get('down')   == upper_neighbor[2]
                    )
            ): target_left_coordinates.append((x, y))
            if (
                    (
                    t.get('target') == lower[0] or 
                    t.get('target') == lower[1] or 
                    t.get('target') == lower[2] or 
                    t.get('target') == lower[4] or 
                    t.get('target') == lower[5] or 
                    t.get('target') == lower[6] or
                    t.get('target') == lower[7]
                    ) and 
                    ( 
                    t.get('left')   == lower_neighbor[0] or
                    t.get('left')   == lower_neighbor[1] or
                    t.get('left')   == lower_neighbor[2] or
                    t.get('left')   == lower_neighbor[3]
                    ) and
                    ( 
                    t.get('up')     == lower_neighbor[0] or
                    t.get('up')     == lower_neighbor[1] or
                    t.get('up')     == lower_neighbor[2] or
                    t.get('up')     == lower_neighbor[3]
                    )
            ): target_right_coordinates.append((x, y))
    coordinates = target_left_coordinates + target_right_coordinates
    return coordinates


def process_single_input(p):
    '''process the path to a single file'''
    def check_path(path):
        p = Path(path)
        if not p.exists() and not p.is_dir() and p.is_file():
            print('No valid path is provided or the file does not exist.')
            input('Press Enter to close to programm.')
            sys.exit(1)
        else:
            return p.parent, p.name
    directory, file = check_path(p)
    str_directory = str(directory)
    return str_directory, [file]


def get_input() -> str:
    '''accepts the user's input'''
    # create a list of files in the folder
    files_lambda = lambda folder: [file for file in os.listdir(folder) if file.lower().endswith('.png') and not file.startswith('Cropped_')]
    # check if the folder is empty
    def is_empty(files_list: list) -> list:
        if not files_list:
            print(print_time(), 'The folder is empty. The program is about to close.')
            close_script()
        else: return files_list
    user_input = input('Enter a path to the PNG files to crop (e.g. D:/screens) or press Enter to use a current directory (type exit to quit): ')
    # add an empty line before the script start
    print()
    # check for a single volume letter
    if user_input.endswith(':'): user_input = user_input + '/'
    match user_input:
        case 'exit':
            print(print_time(), 'The program is about to close.')
            sys.exit(0)
        case 'Exit':
            print(print_time(), 'The program is about to close.')
            sys.exit(0)
        case 'EXIT':
            print(print_time(), 'The program is about to close.')
            sys.exit(0)
        case 'учше':
            print(print_time(), 'The program is about to close.')
            sys.exit(0)
        case 'УЧШЕ':
            print(print_time(), 'The program is about to close.')
            sys.exit(0)
        case '':
            print(print_time(), 'Current directory is being used.')
            directory = os.getcwd()
            files_list = is_empty(files_lambda(directory))
            return directory, files_list
        # match the user input
        case _:
            directory = process_input(user_input)
            files_list = is_empty(files_lambda(directory))
            # e.g. (D:/folder, [screenshot_1.png, screenshot_2.png, ...])
            return directory, files_list
