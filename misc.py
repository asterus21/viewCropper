"""miscellaneous functions

This module contains miscellaneous functions, i.e. those which
- print the current time
- close the script
- process the user's input
- get a list of target pixels
- find target pixels for views
- find target pixels for wizards
"""

import datetime
import os
import sys
from pathlib import Path


def print_time() -> str:
    """prints the current time."""
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


def close_script() -> None:
    """closes the script"""    
    print() # add an empty line before the closing statetement
    input('Press Enter to close the program.')
    sys.exit(0)


def close_script_by_duplicated_flags() -> None:
    """closes the script"""    
    print() # add an empty line before the closing statetement
    print('Both -v and -w flags cannot be given together.')
    input('Press Enter to close the program.')
    sys.exit(1)


def process_input(user_input: str) -> str:
    """validates the user's input"""
    p = Path(user_input)    
    if not p.exists() and not p.is_dir(): # the entered path must exist and be a folder
        print('No valid path is provided.')
        input('Press Enter to close to programm.')
        sys.exit(1)    
    else:
        return user_input


def get_targets(image, x: int, y: int) -> dict:
    """finds target pixels and their neighbours"""
    targets = dict(
        target = image.getpixel((x, y)),
        right  = image.getpixel((x + 1, y)),
        down   = image.getpixel((x, y + 1)),
        left   = image.getpixel((x - 1, y)),
        up     = image.getpixel((x, y - 1))
    )
    return targets


def find_targets(
    image, height: int, width: int, wizard=True, 
    central=None, right=None, left=None,
    upper=None, upper_neighbor=None, lower=None, lower_neighbor=None):
    if wizard:
        target_left_coordinates  = []
        target_right_coordinates = []
        for x in range(width - 1):
            for y in range(height - 1):
                t = get_targets(image, x, y)
                if  (
                    t.get('target') in upper and
                    t.get('right')  in upper_neighbor and
                    t.get('down')   in upper_neighbor
                    ): target_left_coordinates.append((x, y))
                if  (
                    t.get('target') in lower and
                    t.get('left')   in lower_neighbor and
                    t.get('up')     in lower_neighbor    
                    ): target_right_coordinates.append((x, y))
            coordinates = target_left_coordinates + target_right_coordinates
        return coordinates
    else:
        coordinates = []
        for x in range(width - 1):
            for y in range(height - 1):
                t = get_targets(image, x, y) 
                if  (
                    t.get('target') in central and 
                    t.get('right')  in right and
                    t.get('left')   in left
                    ): coordinates.append((x, y))
        return coordinates


def process_single_input(p):
    """process the path to a single file"""
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
    """accepts the user's input"""
    # create a list of files in the folder
    files_lambda = lambda folder: [file for file in os.listdir(folder) if file.lower().endswith('.png') and not file.startswith('Cropped_')]
    # check if the folder is empty
    def is_empty(files_list: list) -> list:
        if not files_list:
            print(print_time(), 'The folder is empty. The program is about to close.')
            close_script()
        else:
            return files_list
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
