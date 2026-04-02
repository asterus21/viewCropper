'''Main script module.

The script is aimed to crop screenshots of the PolyAnalyst nodes.
'''


import os
from PIL import Image
import misc


def remove_empty_values(files: list, values: list) -> tuple:
    '''Removes empty values in a list of found targets.'''
    coordinates = {
        files[i]: values[i] for i in range(0, len(files))
        if values[i]
    }
    return coordinates, list(coordinates.keys())


def find_targets(directory: str, files: list, wizard: bool, stdout: bool) -> dict:
    '''Calls the processing function and removes not processed screenshots.'''
    targets = []
    for file in files:
        if stdout:
            print(f'{misc.print_time()}', 'Processing: ' + file)
            process_targets(directory, file, targets, wizard)
        else:
            process_targets(directory, file, targets, wizard)
    coordinates, screens = remove_empty_values(files, targets)
    return coordinates, screens


def process_targets(directory: str, file: str, targets_list: list, wizard: bool):
    '''Finds targets for both wizards and views.'''
    try:
        from targets import Process
        image = Image.open(os.path.join(directory, file)).convert('RGB')
        width, height = image.size
        process = Process(image, height, width)
        if wizard:
            coordinates = process.find_wizards(whole=True)
        else:
            coordinates = process.find_views()
        targets_list.append(coordinates)
        # print(targets_list)
    except:
        print(misc.print_time(), (f'File {file} not found!'))
        misc.script_close(flags=False)
    return targets_list


def get_coordinates(coordinates: dict, wizard: bool) -> list:
    '''Filters out the target pixels.'''
    if wizard:
        coordinates_list = [
            (item[0], item[-1]) for item in coordinates.values() if item
        ]
    else:
        coordinates_list = [
            item[0] for item in coordinates.values() if item
        ]
    return coordinates_list


def get_keys(values: dict) -> list:
    '''Gets empty keys to process'''
    keys = [
        key for key in values if not values[key]
    ]
    return keys


def get_values(directory: str, files: list, wizard: bool, whole: bool) -> tuple:
    '''Gets values for wizards or views.'''
    targets = []
    if wizard:
        values = {
            file: process_targets(directory, file, targets, whole, wizard=True)
            for file in files
        }
    else:
        values = {
            file: process_targets(directory, file, targets, whole=None, wizard=False)
            for file in files
        }
    coordinates, keys = remove_empty_values(list(values.keys()), list(values.values()))
    return coordinates, keys


def get_types(values: dict, wizard: bool) -> dict:
    '''Returns a file type for a screenshot'''
    if wizard:
        types = {
            key: 'wizard' for key, value in values.items() if value
        }
    else:
        types = {
            key: 'view' for key, value in values.items() if value
        }
    return types


def get_screenshot_types(directory, files, stdout: bool) -> tuple:
    '''Returns the types of screenshots.'''
    wizards      = get_values(directory, files, wizard=True, whole=False)
    views        = get_values(directory, get_keys(wizards), wizard=False, whole=None)
    wizard_types = get_types(wizards, wizard=True)
    view_types   = get_types(views, wizard=False)
    types        = wizard_types | view_types
    sorts        = dict(sorted(types.items()))
    if stdout:
        for key, value in sorts.items(): print(str(key) + ': ' + str(value))
        return sorts
    else:
        return sorts


# def process_views_and_wizards(directory: str, files: list, width: int, height: int) -> None:
#     '''Processes both wizards and views.'''
#     wizards      = get_values(directory, files, wizard=True, whole=True)
#     views        = get_values(directory, get_keys(wizards), wizard=False, whole=False)
#     wizard_types = get_types(wizards, wizard=True)
#     view_types   = get_types(views, wizard=False)
#     crop_wizards(directory, list(wizard_types.keys()), get_coordinates(wizards, wizard=True), stdout=True)
#     crop_views(directory, list(view_types.keys()), get_coordinates(views, wizard=False), width, height, stdout=True)
#     return None


def start_script(folder: str, screens: list, width: int, height: int, wizard: bool, stdout: bool) -> None:
    '''Performs the screenshot cropping process.'''
    from croppers import Croppers
    targets, files = find_targets(folder, screens, wizard, stdout)
    coordinates = get_coordinates(targets, wizard)
    # can be given in a separate function
    croppers = Croppers(folder, files, coordinates, width, height, wizard, stdout)
    croppers.crop_wrapper(croppers.crop_corners)
    return None


def main(wizard: bool, cropped_screens: bool, current_folder: bool, both: bool, type: bool, all: bool, file_path: str, view_width: int, view_height: int) -> None:
    '''Main function of the script.'''
    directory, files = misc.match_path(current_folder, cropped_screens, file_path, all)
    match (both, type):
        case (True, True):
            misc.script_close(flags=True)
        # case (True, False):
            # print(f'{misc.print_time()}', 'Getting a list of files...')
            # process_views_and_wizards(directory, files, view_width, view_height)
        case (False, True):
            print(f'{misc.print_time()}', 'Getting a list of files...')
            get_screenshot_types(directory, files, stdout=True)
        case (False, False):
            print(f'{misc.print_time()}', 'Getting a list of files...')
            start_script(directory, files, view_width, view_height, wizard, stdout=True)
    print(f'{misc.print_time()}', 'The script is finished.')
    misc.script_close(flags=False)
    return None
