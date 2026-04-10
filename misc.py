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
    return now.strftime("%Y-%m-%d %H:%M:%S")


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
        return str(directory), list(file)
    else:
        path = Path(user_input)
        # the entered path must exist and be a folder
        if not path.exists() and path.is_dir():
            print('No valid path is provided.')
            input('Press Enter to close to programm.')
            sys.exit(1)
        else:
            return user_input


def match_path(folder: bool, cropped_screens: bool, path: str, all_files: bool) -> tuple:
    '''Filters out a file, folder and cropped screens.'''
    if folder:
        print(print_time(), 'Current directory is being used...')
        files = get_files(os.getcwd(), cropped_screens, all_files)
        is_empty(files)
    else: directory, files = process_user_input(path, single_file=True) if path else get_input(cropped_screens, all_files)
    return directory, files


def get_files(folder: str, cropped_screens: bool, all_files: bool) -> list:
    '''Gets list of screenshots from a folder.'''
    match (cropped_screens, all_files):
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
                and not file.startswith('Cropped_')
            ]
        case(False, False):
            files = [
                file for file in os.listdir(folder)
                if file.lower().endswith('.png')
                and file.startswith('Screenshot_')
            ]
    return files


def is_empty(files_list: list) -> list:
    '''Checks if the given list of files is empty.'''
    if not files_list:
        print(print_time(), 'No PNG files found. The program is about to close.')
        script_close(flags=False)
    else:
        return files_list


def process_directory(folder, if_cropped, if_all) -> tuple:
    '''Processes a folder and files to get screenshots from.'''
    return folder, get_files(folder, if_cropped, if_all)


def get_input(cropped_screens: bool, all_files: bool) -> tuple:
    '''Accepts the user's input.'''
    user_input = input('Enter a path to the PNG files to crop (e.g. D:/screens) or press Enter to use a current directory (type exit to quit): ')
    # adds an empty line before the script start
    print()
    # checks for a single volume letter
    if user_input.endswith(':'): user_input = user_input + '/'
    if user_input in ('exit', 'Exit', 'EXIT', 'учше', 'УЧШЕ'):
        print(print_time(), 'The program is about to close.')
        sys.exit(0)
    elif user_input == '':
        print(print_time(), 'Current directory is being used.\n')
        folder, files = process_directory(os.getcwd(), cropped_screens, all_files)
    else:
        directory = process_user_input(user_input, single_file=False)
        folder, files = process_directory(directory, cropped_screens, all_files)
    return folder, files
