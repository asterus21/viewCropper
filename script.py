'''Main script module.

The script is aimed to crop screenshots of the PolyAnalyst nodes.
'''

import misc as misc

from classes.croppers import Croppers
from classes.targets import Targets
from classes.screenshot_types import Types


def main(wizard: bool, cropped_screens: bool, current_folder: bool, both: bool, type: bool, all_files: bool, file_path: str, view_width: int, view_height: int) -> object:
    '''Main function of the script.'''
    directory, files = misc.match_path(current_folder, cropped_screens, all_files, file_path)
    match (both, type):
        case (True, True):
            misc.script_close(flags=True)
        case (True, False):
            print(f'{misc.print_time()}', 'Getting a list of files...')
            process_views_and_wizards(directory, files, view_width, view_height)
        case (False, True):
            print(f'{misc.print_time()}', 'Getting a list of files...')
            get_screenshot_types(directory, files)
        case (False, False):
            print(f'{misc.print_time()}', 'Getting a list of files...')
            screenshots, coordinates = process_files(directory, files, wizard, stdout=True)
            start_script(directory, screenshots, coordinates, view_width, view_height, wizard, stdout=True)
    print(f'{misc.print_time()}', 'The script is finished.')


def process_views_and_wizards(directory: str, files: list, width: int, height: int) -> object:
    '''Processes both wizards and views.'''
    wizards, wizard_coordinates = process_files(directory, files, wizard=True, stdout=False)
    views, view_coordinates     = process_files(directory, files, wizard=False, stdout=False)
    start_script(directory, wizards, wizard_coordinates, width=None, height=None, wizard=True, stdout=False)
    start_script(directory, views, view_coordinates, width, height, wizard=False, stdout=False)
    print(f'{misc.print_time()}', str(len(wizards) + len(views)) + ' file(s) processed.')


def get_screenshot_types(directory, files) -> dict:
    '''Returns the types of screenshots.'''
    types = Types(directory, files)
    return types.get_screenshot_types()


def process_files(folder: str, screens: list, wizard: bool, stdout: bool) -> tuple:
    '''Gets a list of files and returns targets coordinates.'''
    targets_instance = Targets(folder, screens, wizard, stdout)
    targets, files = targets_instance.find_targets(type=False, whole=True)
    coordinates = targets_instance.get_coordinates(targets)
    return files, coordinates

def start_script(folder: str, files: list, coordinates: list, width: int, height: int, wizard: bool, stdout: bool) -> object:
    '''Performs the screenshot cropping process.'''
    crop = Croppers(folder, files, coordinates, width, height, wizard, stdout)
    return crop.crop_screenshots(crop.crop_corners)
