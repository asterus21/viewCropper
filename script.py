'''
The script is aimed to crop screenshots of the PolyAnalyst nodes.
'''

import os

from PIL import Image

import data
import misc


def find_target_pixels(directory: str, files: list, wizard: bool) -> dict:
    '''Calls the targets processing function and removes not processed screenshots.'''
    targets = []
    print(f'{misc.print_time()}', 'Getting a list of files...')
    for file in files:
        print(f'{misc.print_time()}', 'Processing: ' + file)
        process_targets(directory, file, targets, wizard)
    # remove empty coordinates
    coordinates = misc.remove_empty_values(files, targets)
    return coordinates


# create a list of coordinates for the target pixels
def process_targets(directory: str, file: str, targets: list, wizard: bool):
    '''Finds targets for both wizards and views.'''
    # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png') then convert to the RGB format
    image = Image.open(os.path.join(directory, file)).convert('RGB')
    width, height = image.size
    if wizard:
        coordinates = misc.find_targets(
            image,
            height,
            width,
            wizard=True,
            upper=data.upper_targets,
            upper_neighbor=data.upper_neighbor_targets,
            lower=data.lower_targets,
            lower_neighbor=data.lower_neighbor_targets
            )
    else:
        coordinates = misc.find_targets(
            image,
            height,
            width,
            wizard=False,
            central=data.central_targets,
            right=data.right_targets,
            left=data.left_targets
            )
    targets.append(coordinates)
    return targets


def process_wizards(directory: str, file: str, targets: list):
    '''Finds targets only for wizards.'''
    image = Image.open(os.path.join(directory, file)).convert('RGB')
    width, height = image.size
    coordinates = misc.find_targets(
        image,
        height,
        width,
        wizard=True,
        upper=data.upper_targets,
        upper_neighbor=data.upper_neighbor_targets,
        lower=data.lower_targets,
        lower_neighbor=data.lower_neighbor_targets
        )
    targets.append(coordinates)
    return targets


def process_views(directory: str, file: str, targets: list):
    '''Finds targets only for views.'''
    image = Image.open(os.path.join(directory, file)).convert('RGB')
    width, height = image.size
    coordinates = misc.find_targets(
        image,
        height,
        width,
        wizard=False,
        central=data.central_targets,
        right=data.right_targets,
        left=data.left_targets
    )
    targets.append(coordinates)
    return targets


def get_new_list_of_files(files: dict) -> list:
    '''Returns dictionary keys with only the screenshots to be processed.'''
    # fetch only the keys of the dictionary, i.e. files names
    # because those file names are then given as arguments
    # to crop only needed screenshots as we don't want to crop extra ones
    return(list(files.keys()))


def get_coordinates(coordinates: dict, wizard: bool) -> list:
    '''Filters out the target pixels.'''
    # fetch only the first target in case there are several ones
    if not wizard:
        coordinates_list = [
            item[0] for item in coordinates.values() if item
        ]
    # fetch only the first and last targets for wizards in case there are several ones
    else:
        coordinates_list = [
            (item[0], item[-1]) for item in coordinates.values() if item
        ]
    return coordinates_list


# main logic of the script, i.e. image cropping
def crop_corners(directory: str, files: list, target_pixels: list, view_width: int, view_height: int, wizard: bool) -> None:
    '''Crops the screenshots according to the target pixels.'''
    file_number = 1
    cropped_files = len(misc.get_files(os.getcwd(), cropped=True))
    for i in range(len(files)):
        # skip empty coordinates if present
        if not target_pixels[i]: continue
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
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
                if cropped_files:
                    crop.save(f'Cropped_{cropped_files+1}.png')
                    cropped_files += 1
                else:
                    crop.save(f'Cropped_{file_number}.png')
                    file_number += 1
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
    print(f'{misc.print_time()}', str(len(files)) + ' file(s) processed.')
    return None


def show_screenshot_types(current_folder: bool) -> list:
    '''Returns the types of screenshots.'''
    if current_folder:
        directory = os.getcwd()
        files = misc.get_files(directory, cropped=False)
    else:
        directory, files = misc.get_input(cropped=False)
    views_targets, wizards_targtes = [], []
    for file in files:
        process_targets(directory, file, views_targets, wizard=False)
        process_targets(directory, file, wizards_targtes, wizard=True)

    def get_target_pixels(directory: str, files: list) -> list:
        '''Creates a dictionary with the types of screenshots.'''
        targets = []
        for file in files:
            process_targets(directory, file, targets, wizard=True)
        coordinates = {
            files[i]: targets[i] for i in range(0, len(files))
        }
        types = {
            key: "wizard" if value else "view" for key, value in coordinates.items()
        }
        print()
        for key, value in types.items():
            print(str(key) + ': ' + str(value))
        print()
        return types

    merged = list(misc.remove_empty_values(files, views_targets).keys()) + list(misc.remove_empty_values(files, wizards_targtes).keys())
    get_target_pixels(directory, sorted(merged))
    return sorted(merged)


def match_path_and_screenshots(folder: bool, path: str, screens: bool) -> tuple:
    '''Filters out a file, folder and cropped screens.'''
    match (folder, screens):
        case(True, True):
            directory = os.getcwd()
            files = misc.get_files(directory, cropped=True)
            misc.is_empty(files)
        case(True, False):
            directory = os.getcwd()
            files = misc.get_files(directory, cropped=False)
            misc.is_empty(files)
        case(False, False):
            directory, files = misc.process_user_input(path, single_file=True) if path else misc.get_input(cropped=False)
        case(False, True):
            directory, files = misc.process_user_input(path, single_file=True) if path else misc.get_input(cropped=True)
    return directory, files


def start_script(folder: str, screens: bool, width: int, height: int, wizard: bool) -> None:
    '''Performs the screenshot cropping process.'''
    targets = find_target_pixels(folder, screens, wizard)
    files_list = get_new_list_of_files(targets)
    edited_coordinates = get_coordinates(targets, wizard)
    crop_corners(
        folder,
        files_list,
        edited_coordinates,
        width,
        height,     
        wizard
        )
    print(f'{misc.print_time()}', 'The script is finished.')


def main(wizard: bool, file_path: bool, cropped: bool, current_folder: bool, both: bool, view_width: int, view_height: int) -> None:
    '''Main function of the script.'''
    directory, files = match_path_and_screenshots(current_folder, file_path, cropped)
    if both:
        start_script(directory, files, view_width, view_height, wizard=True)
        start_script(directory, files, view_width, view_height, wizard=False)
        misc.script_close(False)
    else:
        start_script(directory, files, wizard, view_width, view_height)
        misc.script_close(False)
