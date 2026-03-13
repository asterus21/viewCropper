'''
The script is aimed to crop screenshots of the PolyAnalyst nodes.
'''

import os
from PIL import Image
import data
import misc


# create a list of coordinates for the target pixels
def process_targets(directory: str, files: list, wizard: bool, targets: list):
    '''finds targets for both wizards and views'''
    targets = []
    # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png') then convert to the RGB format
    for file in files:
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
    targets_as_dictionary = dict(zip(files, targets))
    return targets_as_dictionary


def process_wizards(directory: str, files: list, targets: list):
    '''finds targets only for wizards'''
    for file in files:
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


def process_views(directory: str, files: list, targets: list):
    '''finds targets only for views'''
    for file in files:
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


def find_target_pixels(directory: str, files: list, wizard: bool) -> list:
    '''calls the targets processing function and removes not processed screenshots'''
    targets = []
    print(f'{misc.print_time()}', 'Getting a list of files...')
    for file in files:
        print(f'{misc.print_time()}', 'Processing: ' + file)
        process_targets(directory, file, targets, wizard)
    # remove empty coordinates
    coordinates = {
        files[i]: targets[i] for i in range(0, len(files))
        if targets[i]
    }
    return coordinates


def get_target_pixels(directory: str, files: list) -> list:
    '''shows the type of screenshots'''
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


def get_new_list_of_files(files: dict) -> list:
    # fetch only the keys of the dictionary, i.e. files names
    # because those file names are then given as arguments
    # to crop the screenshots as we don't want to crop extra ones
    return(list(files.keys()))


def get_coordinates(coordinates: dict, wizard: bool) -> list:
    # fetch only the first target in case there are several ones
    if not wizard:
        coordinates_list = [
            item[0] for item in coordinates.values() if item
        ]
    # fetch only the first and last targets for wizards
    else:
        coordinates_list = [
            (item[0], item[-1]) for item in coordinates.values() if item
        ]
    return coordinates_list


# main logic of the script, i.e. image cropping
def crop_corners(directory: str, files: list, target_pixels: list, wizard: bool, view_width: int, view_height: int) -> None:
    file_number = 1
    for i in range(len(files)):
        # skip empty coordinates
        if not target_pixels[i]: continue
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
        image = Image.open(os.path.join(directory, files[i]))
        # main logic of the script, i.e. screens cropping
        if not wizard:
            crop = image.crop((
                target_pixels[i][0] - 12,
                target_pixels[i][1] - 15,
                view_width,
                view_height
                ))
            crop.save(f'Cropped_{file_number}.png')
        else:
            crop = image.crop((
                target_pixels[i][0][0],
                target_pixels[i][0][1],
                target_pixels[i][1][0] + 1,
                target_pixels[i][1][1] + 1
                ))
            crop.save(f'Cropped_{file_number}.png')
        file_number += 1
    # cropped_files = [file for file in os.listdir(directory) if file.startswith('Cropped_')]
    # print(f'{misc.print_time()}', str(len(cropped_files)) + ' file(s) processed.')


def start_script_for_both_wizards_and_views(current_folder: bool, view_width: int, view_height: int) -> tuple:
    if current_folder:
        directory, files = os.getcwd(), misc.get_files(directory, cropped=False)
    else:
        directory, files = misc.get_input(cropped=False)
    views = process_targets(directory, files, targets=[], wizard=False)
    wizards = process_targets(directory, files, targets=[], wizard=True)
    print(views, wizards)


def main(wizard: bool, file_path: bool, cropped: bool, current_folder: bool, view_width: int, view_height: int) -> None:
    '''main function of the script'''
    match (current_folder, cropped):
        case(True, True):   
            directory = os.getcwd()
            files = misc.get_files(directory, cropped=True)
        case(True, False):  
            directory = os.getcwd()
            files = misc.get_files(directory, cropped=False) 
        case(False, False): 
            directory, files = misc.process_user_input(file_path, single_file=True) if file_path else misc.get_input(cropped=False)
        case(False, True):  
            directory, files = misc.process_user_input(file_path, single_file=True) if file_path else misc.get_input(cropped=True)       
    targets = find_target_pixels(directory, files, wizard)
    files_list = get_new_list_of_files(targets)
    edited_coordinates = get_coordinates(targets, wizard)
    crop_corners(
        directory, 
        files_list, 
        edited_coordinates, 
        wizard, 
        view_width, 
        view_height
        )
    print(f'{misc.print_time()}', 'The script is finished.')
    misc.script_close(False)
