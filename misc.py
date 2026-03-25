'''Miscellaneuos functions module.

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


def script_close(flags: bool) -> None:
    '''Closes the script.'''
    # adds an empty line before the closing statetement
    print()
    if flags:
        input('Given flags cannot be used together.\nPress Enter to close the program.')
        sys.exit(1)
    else:
        input('Press Enter to close the program.')
        sys.exit(0)


def check_path(path):
    '''Checks if the entered path is a file.'''
    user_input = Path(path)
    # the entered path must exist and be a file and not a folder
    if not user_input.exists() and not user_input.is_dir() and user_input.is_file():
        print('No valid path is provided or the file does not exist.')
        input('Press Enter to close to programm.')
        sys.exit(1)
    else:
        return user_input.parent, user_input.name


def process_user_input(user_input: str, single_file: bool):
    '''Processes user's input.'''
    if single_file:
        directory, file = check_path(user_input)
        folder = str(directory)
        return folder, [file]
    else:
        path = Path(user_input)
        # the entered path must exist and be a folder
        if not path.exists() and path.is_dir():
            print('No valid path is provided.')
            input('Press Enter to close to programm.')
            sys.exit(1)
        else:
            return user_input


def get_targets(image, x: int, y: int) -> dict:
    '''Finds target pixels and their neighbours.'''
    targets = dict(
        target = image.getpixel((x, y)),
        right  = image.getpixel((x + 1, y)),
        down   = image.getpixel((x, y + 1)),
        left   = image.getpixel((x - 1, y)),
        up     = image.getpixel((x, y - 1))
    )
    return targets


def find_wizards(image, height: int, width: int, whole: bool, upper=None, upper_neighbor=None, lower=None, lower_neighbor=None):
    if whole:
        target_left_coordinates  = []
        target_right_coordinates = []
        for x in range(width - 1):
            for y in range(height - 1):
                t = get_targets(image, x, y)
                if  (
                    t.get('target') in upper and
                    t.get('right')  in upper_neighbor and
                    t.get('down')   in upper_neighbor
                    ):
                    target_left_coordinates.append((x, y))
                if  (
                    t.get('target') in lower and
                    t.get('left')   in lower_neighbor and
                    t.get('up')     in lower_neighbor
                    ):
                    target_right_coordinates.append((x, y))
            coordinates = target_left_coordinates + target_right_coordinates
    else:
        coordinates = []
        for x in range(width - 1):
            for y in range(height - 1):
                t = get_targets(image, x, y)
                if  (
                    t.get('target') in upper and
                    t.get('right')  in upper_neighbor and
                    t.get('down')   in upper_neighbor
                    ):
                    coordinates.append((x, y))
    return coordinates


def find_views(image, height: int, width: int, central=None, right=None, left=None):
    coordinates = []
    for x in range(width - 1):
        for y in range(height - 1):
            t = get_targets(image, x, y)
            if  (
                t.get('target') in central and
                t.get('right')  in right and
                t.get('left')   in left
                ):
                coordinates.append((x, y))
    return coordinates


def find_targets(
    image, height: int, width: int, wizard: bool,
    central=None, right=None, left=None, upper=None, upper_neighbor=None, lower=None, lower_neighbor=None) -> list:
    '''Finds target pixels by their RGB value.'''
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
                    ):
                    target_left_coordinates.append((x, y))
                if  (
                    t.get('target') in lower and
                    t.get('left')   in lower_neighbor and
                    t.get('up')     in lower_neighbor
                    ):
                    target_right_coordinates.append((x, y))
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
                    ):
                    coordinates.append((x, y))
        return coordinates


def match_path(folder: bool, cropped_screens: bool, path: str, strict: bool) -> tuple:
    '''Filters out a file, folder and cropped screens.'''
    if folder:
            print(print_time(), 'Current directory is being used...')
            directory = os.getcwd()
            files = get_files(directory, cropped_screens, strict)
            # print(directory, files)
            is_empty(files)
    else:
        directory, files = process_user_input(path, single_file=True) if path else get_input(cropped_screens, strict)
    return directory, files


def get_files(folder: str, cropped_screens: bool, strict: bool) -> list:
    '''Gets list of screenshots from a folder.'''
    match (cropped_screens, strict):
        case(True, True):
            script_close(flags=True)
        case(True, False):
            files = [
                file for file in os.listdir(folder)
                if file.lower().endswith('.png')
                and file.startswith('Cropped_')
            ]
        case(False, True):
            files = [
                file for file in os.listdir(folder)
                if file.lower().endswith('.png')
                and file.startswith('Screenshot_')
            ]
        case(False, False):
            files = [
                file for file in os.listdir(folder)
                if file.lower().endswith('.png')
                and not file.startswith('Cropped_')
            ]
    return files


def is_empty(files_list: list) -> list:
    '''Checks if the given list of files is empty.'''
    if not files_list:
        print(print_time(), 'No PNG files found. The program is about to close.')
        script_close(flags=False)
    else:
        return files_list


def get_input(cropped_screens: bool, strict: bool) -> str:
    '''Accepts the user's input.'''
    user_input = input('Enter a path to the PNG files to crop (e.g. D:/screens) or press Enter to use a current directory (type exit to quit): ')
    # adds an empty line before the script start
    print()
    # checks for a single volume letter
    if user_input.endswith(':'):
        user_input = user_input + '/'
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
            print(print_time(), 'Current directory is being used.\n')
            directory = os.getcwd()
            files_list = get_files(directory, cropped_screens, strict)
            is_empty(files_list)
            return directory, files_list
        case _:
            directory = process_user_input(user_input, single_file=False)
            files_list = get_files(directory, cropped_screens, strict)
            is_empty(files_list)
            # D:/folder, [screenshot_1.png, screenshot_2.png, ...]
            return directory, files_list
