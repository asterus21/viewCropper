'''The script is aimed to crop screenshots of the PolyAnalyst nodes.'''

import os
from PIL import Image
import data
import misc


# TODO: add docstrings
# TODO: add -s flag to show the sizes of views
# TODO: add -h flag to show the manual
# TODO: add full flags, e.g. --wizard


# create a list of coordinates for the target pixels
def find_target_pixels(directory: str, files: list, wizard=True) -> list:
    targets = []
    print(f'{misc.print_time()}', 'Getting a list of files...')
    for file in files:
        print(f'{misc.print_time()}', 'Processing: ' + file)
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
        # and convert to the RGB format
        image = Image.open(os.path.join(directory, file)).convert('RGB')
        width, height = image.size
        if wizard:
            coordinates = misc.find_targets_in_wizard(
                image,
                height,
                width,
                data.upper_targets, 
                data.upper_neighbor_targets, 
                data.lower_targets,
                data.lower_neighbor_targets
                )
        else: 
            coordinates = misc.find_targets_in_view(
                image,
                height,
                width,
                data.central_targets,
                data.right_targets,
                data.left_targets                    
                )
        targets.append(coordinates)
    # remove empty coordinates
    non_empty_coordinates = {
            files[i]: targets[i] 
            for i in range(0, len(files))
            if targets[i]
    }
    return non_empty_coordinates


def get_new_list_of_files(files: dict) -> list:
    # fetch only the keys of the dictionary, i.e. files names
    # because those file names are then given as arguments
    # to crop the screenshots as we don't want to crop extra ones
    return(list(files.keys()))


def edit_coordinates(coordinates: dict, wizard=True) -> list:
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
def crop_corners(directory: str, files: list, target_pixels: list, wizard=True, view_width=1271, view_height=761) -> None:
    file_number = 1
    for i in range(len(files)):
        # skip empty coordinates
        if not target_pixels[i]: continue
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
        image = Image.open(os.path.join(directory, files[i]))
        # main logic of the script, i.e. screens cropping
        if not wizard:
            crop = image.crop((
                # target_pixels[i][0][0] - 12,
                # target_pixels[i][0][1] - 15,
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
    cropped_files = [file for file in os.listdir(directory) if file.startswith('Cropped_')]
    print(f'{misc.print_time()}', str(len(cropped_files)) + ' file(s) processed.')


def main(directory, files, wizard, view_width, view_height):
    ##################################
    # find target pixels
    targets = find_target_pixels(directory, files, wizard)
    ##################################
    # get a new list of files, i.e. remove those where there are no targets
    # i.e. here we filter out those filenames which do not have empty targets
    non_empty_files = get_new_list_of_files(targets)
    ##################################
    # edit the list, i.e. get only the first occurence for views
    # and the first and last coordinates for wizards
    edited_coordinates = edit_coordinates(targets, wizard)
    ##################################
    # cropping the images
    crop_corners(
        directory, 
        non_empty_files, 
        edited_coordinates, 
        wizard, 
        view_width, 
        view_height
        )
    ##################################
    # close the script
    print(f'{misc.print_time()}', 'The script is finished.')
    misc.close_script()
