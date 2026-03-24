'''Main script module.

The script is aimed to crop screenshots of the PolyAnalyst nodes.
'''


import os

from PIL import Image

import data
import misc


def remove_empty_values(files: list, values: list) -> dict:
    '''Removes empty values in a list of found targets.'''
    coordinates = {
        files[i]: values[i] for i in range(0, len(files))
        if values[i]
    }
    return coordinates


def find_target_pixels(directory: str, files: list, wizard: bool, stdout: bool) -> dict:
    '''Calls the processing function and removes not processed screenshots.'''
    targets = []
    for file in files:
        if stdout:
            print(f'{misc.print_time()}', 'Processing: ' + file)
            process_targets(directory, file, targets, wizard)
        else:
            process_targets(directory, file, targets, wizard)
    coordinates = remove_empty_values(files, targets)
    return coordinates


def process_targets(directory: str, file: str, targets: list, wizard: bool):
    '''Finds targets for both wizards and views.'''
    try:
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png') then convert to the RGB format
        image = Image.open(os.path.join(directory, file)).convert('RGB')
        width, height = image.size
        if wizard:
            coordinates = misc.find_targets(
                image,
                height,
                width,
                wizard=True,
                upper=data.UPPER_TARGETS,
                upper_neighbor=data.UPPER_NEIGHBOR_TARGETS,
                lower=data.LOWER_TARGETS,
                lower_neighbor=data.LOWER_NEIGHBOR_TARGETS
                )
        else:
            coordinates = misc.find_targets(
                image,
                height,
                width,
                wizard=False,
                central=data.CENTRAL_TARGETS,
                right=data.RIGHT_TARGETS,
                left=data.LEFT_TARGETS
                )
        targets.append(coordinates)
    except:
        print(misc.print_time(), (f'File {file} not found!'))
        misc.script_close(flags=False)
    return targets


def process_wizards(directory: str, file: str, whole: bool) -> list:
    '''Finds a part of targets only for wizards.'''
    image = Image.open(os.path.join(directory, file)).convert('RGB')
    width, height = image.size
    processed = misc.find_wizards(
        image,
        height,
        width,
        whole,
        upper=data.UPPER_TARGETS,
        upper_neighbor=data.UPPER_NEIGHBOR_TARGETS,
        lower=data.LOWER_TARGETS,
        lower_neighbor=data.LOWER_NEIGHBOR_TARGETS
        )
    return processed


def process_views(directory: str, file: str) -> list:
    '''Finds targets only for views.'''
    image = Image.open(os.path.join(directory, file)).convert('RGB')
    width, height = image.size
    processed = misc.find_views(
        image,
        height,
        width,
        central=data.CENTRAL_TARGETS,
        right=data.RIGHT_TARGETS,
        left=data.LEFT_TARGETS
        )
    return processed


def get_new_list_of_files(files: dict) -> list:
    '''Returns dictionary keys with only the screenshots to be processed.'''
    # fetches only the keys of the dictionary, i.e. files names
    # to crop only needed screenshots as we don't want to crop extra ones
    return(list(files.keys()))


def get_coordinates(coordinates: dict, wizard: bool) -> list:
    '''Filters out the target pixels.'''
    # fetches only the first target in case there are several ones
    if not wizard:
        coordinates_list = [
            item[0] for item in coordinates.values() if item
        ]
    # fetches only the first and last targets for wizards in case there are several ones
    else:
        coordinates_list = [
            (item[0], item[-1]) for item in coordinates.values() if item
        ]
    return coordinates_list


# main logic of the script, i.e. image cropping
def crop_corners(directory: str, files: list, target_pixels: list, view_width: int, view_height: int, wizard: bool, stdout: bool) -> None:
    '''Crops the screenshots according to the target pixels.'''
    file_number = 1
    cropped_files = len(misc.get_files(folder=os.getcwd(), cropped=True, strict=False))
    for i in range(len(files)):
        # skips empty coordinates if present
        if not target_pixels[i]:
            continue
        # concatenates a path and file, e.g. 'D:/folder/screenshot_1.png')
        image = Image.open(os.path.join(directory, files[i]))
        # main logic of the script, i.e. screens cropping
        try:
            if not wizard:
                crop = image.crop((
                    target_pixels[i][0] - 12,
                    target_pixels[i][1] - 15,
                    view_width,
                    view_height
                    ))
            else:
                crop = image.crop((
                    target_pixels[i][0][0],
                    target_pixels[i][0][1],
                    target_pixels[i][1][0] + 1,
                    target_pixels[i][1][1] + 1
                    ))
            if cropped_files:
                crop.save(f'Cropped_{cropped_files+1}.png')
                cropped_files += 1
            else:
                crop.save(f'Cropped_{file_number}.png')
                file_number += 1
        except Exception as E:
            print(f'{E}: no wizard screenshot or view one is found.')
    if stdout:
        print(f'{misc.print_time()}', str(len(files)) + ' file(s) processed.')
    return None


def crop_wizards(directory: str, files: list, target_pixels: list, stdout: bool) -> None:
    '''Crops the screenshots according to the target pixels.'''
    file_number = 1
    cropped_files = len(misc.get_files(folder=os.getcwd(), cropped=True, strict=False))
    for i in range(len(files)):
        # skips empty coordinates if present
        if not target_pixels[i]:
            continue
        # concatenates a path and file, e.g. 'D:/folder/screenshot_1.png')
        image = Image.open(os.path.join(directory, files[i]))
        # main logic of the script, i.e. screens cropping
        try:
            crop = image.crop((
                target_pixels[i][0][0],
                target_pixels[i][0][1],
                target_pixels[i][1][0] + 1,
                target_pixels[i][1][1] + 1
                ))
            if cropped_files:
                crop.save(f'Cropped_{cropped_files+1}.png')
                cropped_files += 1
            else:
                crop.save(f'Cropped_{file_number}.png')
                file_number += 1
        except Exception as E:
            print(f'{E}: no wizard screenshot is found.')
    if stdout:
        print(f'{misc.print_time()}', str(len(files)) + ' file(s) processed.')
    return None


def crop_views(directory: str, files: list, target_pixels: list, view_width: int, view_height: int, stdout: bool) -> None:
    '''Crops the screenshots according to the target pixels.'''
    file_number = 1
    cropped_files = len(misc.get_files(folder=os.getcwd(), cropped=True, strict=False))
    for i in range(len(files)):
        # skips empty coordinates if present
        if not target_pixels[i]:
            continue
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
        image = Image.open(os.path.join(directory, files[i]))
        # main logic of the script, i.e. screens cropping
        try:
            crop = image.crop((
                target_pixels[i][0] - 12,
                target_pixels[i][1] - 15,
                view_width,
                view_height
                ))
            if cropped_files:
                crop.save(f'Cropped_{cropped_files+1}.png')
                cropped_files += 1
            else:
                crop.save(f'Cropped_{file_number}.png')
                file_number += 1
        except Exception as E:
            print(f'{E}: no wizard screenshot or view one is found.')
    if stdout:
        print(f'{misc.print_time()}', str(len(files)) + ' file(s) processed.')
    return None


def get_keys(values: dict) -> list:
    '''Gets empty keys to process'''
    keys = [
        key for key in values if not values[key]
    ]
    return keys


def get_values(directory: str, files: list, wizard: bool, whole: bool) -> dict:
    '''Gets values for wizards or views.'''
    if wizard:
        values = {
            file: process_wizards(directory, file, whole)
            for file in files
        }
    else:
        values = {
            file: process_views(directory, file)
            for file in files
        }
    return values


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


def process_views_and_wizards(directory: str, files: list, width: int, height: int) -> None:
    '''Processes both wizards and views.'''
    wizards      = get_values(directory, files, wizard=True, whole=True)
    views        = get_values(directory, get_keys(wizards), wizard=False, whole=False)
    wizard_types = get_types(wizards, wizard=True)
    view_types   = get_types(views, wizard=False)
    crop_wizards(directory, list(wizard_types.keys()), get_coordinates(wizards, wizard=True), stdout=True)
    crop_views(directory, list(view_types.keys()), get_coordinates(views, wizard=False), width, height, stdout=True)
    return None


def start_script(folder: str, screens: list, width: int, height: int, wizard: bool, stdout: bool) -> None:
    '''Performs the screenshot cropping process.'''
    targets = find_target_pixels(folder, screens, wizard, stdout)
    files_list = get_new_list_of_files(targets)
    edited_coordinates = get_coordinates(targets, wizard)
    crop_corners(
        folder,
        files_list,
        edited_coordinates,
        width,
        height,
        wizard,
        stdout
        )
    return None


def main(wizard: bool, cropped_screens: bool, current_folder: bool, both: bool, type: bool, strict: bool, file_path: str, view_width: int, view_height: int) -> None:
    '''Main function of the script.'''
    directory, files = misc.match_path(current_folder, cropped_screens, file_path, strict)
    match(both, type):
        case(True, True):
            misc.script_close(flags=True)
        case(True, False):
            process_views_and_wizards(
                directory,
                files,
                view_width,
                view_height
            )
        case(False, True):
            print(f'{misc.print_time()}', 'Getting a list of files...')
            get_screenshot_types(directory, files, stdout=True)
        case(False, False):
            print(f'{misc.print_time()}', 'Getting a list of files...')
            start_script(directory, files, view_width, view_height, wizard, stdout=True)
        case _:
            print(f'{misc.print_time()}', 'Getting a list of files...')
            start_script(directory, files, view_width, view_height, wizard, stdout=True)
    print(f'{misc.print_time()}', 'The script is finished.')
    misc.script_close(flags=False)
    return None
