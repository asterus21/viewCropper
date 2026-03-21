'''Main script module.

The script is aimed to crop screenshots of the PolyAnalyst nodes.
'''


import os

from PIL import Image

import data
import misc


def find_target_pixels(directory: str, files: list, wizard: bool, stdout: bool) -> dict:
    '''Calls the targets processing function and removes not processed screenshots.'''
    targets = []
    for file in files:
        if stdout:
            print(f'{misc.print_time()}', 'Processing: ' + file)
            process_targets(directory, file, targets, wizard)
        else:
            process_targets(directory, file, targets, wizard)
    # remove empty coordinates
    coordinates = misc.remove_empty_values(files, targets)
    return coordinates


def process_targets(directory: str, file: str, targets: list, wizard: bool):
    '''Finds targets for both wizards and views.'''
    # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png') then convert to the RGB format
    try:
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


def process_wizards(directory: str, file: str) -> list:
    '''Finds targets only for wizards.'''
    image = Image.open(os.path.join(directory, file)).convert('RGB')
    width, height = image.size
    processed = misc.find_wizards(
        image,
        height,
        width,
        upper=data.UPPER_TARGETS,
        upper_neighbor=data.UPPER_NEIGHBOR_TARGETS
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
    # fetch only the keys of the dictionary, i.e. files names
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
# TODO: split the function into two functions
def crop_corners(directory: str, files: list, target_pixels: list, view_width: int, view_height: int, wizard: bool, stdout: bool) -> None:
    '''Crops the screenshots according to the target pixels.'''
    file_number = 1
    cropped_files = len(misc.get_files(folder=os.getcwd(), cropped=True))
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
    if stdout:
        print(f'{misc.print_time()}', str(len(files)) + ' file(s) processed.')
    return None


def show_screenshot_types(current_folder: bool, stdout: bool, test: bool) -> tuple:
    '''Returns the types of screenshots.'''
    # make a restriction that only files named 'Screenshot_'
    # can be used for the -b flag
    # then call the process_targets() function
    # to process only views and not wisards
    # as there are less targets to process
    # then call coordinates() and types()
    # perhaps there's a way to merge these functions
    # and make a restriction to use the -b and -f flags
    # as well as the -b and -v and -w and -c ones
    # in this case we call the process_targets() function 
    # only once and not more
    # IMPORTANT: leave the old behaviour 
    # IMPORTANT: for the -t flag
    # IMPORTANT: and let the user decide
    # IMPORTANT: whether to use the 'screenshot' value
    # IMPORTANT: in the misc.get_files()
    # IMPORTANT: to show the types of only those files
    # IMPORTANT: which start with Screenshot_
    # IMPORTANT: it will be needed
    # IMPORTANT: to add a a flag
    # IMPORTANT: for the new and old behaviour
    # add type and name flags
    # if both true, then show types for Screenshot_ only files
    # if true and false, then use the old behavior
    # if false and none, then process Screenshot_ only files
    if current_folder:
        print(misc.print_time(), 'Current directory is being used...')
        directory = os.getcwd()
        files = misc.get_files(directory, cropped=False)
    else:
        directory, files = misc.get_input(cropped=False)

    def get_values(directory: str, files: list, wizard: bool) -> dict:
        '''Gets values for wizards or views.'''
        if wizard:
            values = {
                file: process_wizards(directory, file)
                for file in files
            }
        else:
            values = {
                file: process_views(directory, file)
                for file in files
            }
        return values
    
    def get_keys(values: dict) -> list:
        '''Gets empty keys to process'''
        keys = [
            key for key in values if not values[key]
        ]
        return keys

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

    # TODO: add test:bool to test the current behavior
    # TODO: old one with the call of the process_targets() function
    # TODO: and the use of the dictionary comprehensions for both wizards and views
    # TODO: then merge the dictionaries without calling the get_key() function
    if test:
        wizards      = get_values(directory, files, wizard=True)
        keys         = get_keys(wizards)
        views        = get_values(directory, keys, wizard=False)
        wizard_types = get_types(wizards, wizard=True)
        view_types   = get_types(views, wizard=False)
        types        = wizard_types | view_types
        sorts        = dict(sorted(types.items()))
    else:
        wizards      = get_values(directory, files, wizard=True)
        views        = get_values(directory, files, wizard=False)
        wizard_types = get_types(wizards, wizard=True)
        view_types   = get_types(views, wizard=False)
        wizard_types.update({key: value for key, value in view_types.items()})        
        sorts        = dict(sorted(wizard_types.items()))
        
    if stdout:
        for key, value in sorts.items():
            print(str(key) + ': ' + str(value))
    else:
        return sorts


def match_path(folder: bool, path: bool, cropped_screens: bool) -> tuple:
    '''Filters out a file, folder and cropped screens.'''
    match (folder, cropped_screens):
        case(True, True):
            print(misc.print_time(), 'Current directory is being used...')
            directory = os.getcwd()
            files = misc.get_files(directory, cropped=True)
            misc.is_empty(files)
        case(True, False):
            print(misc.print_time(), 'Current directory is being used...')
            directory = os.getcwd()
            files = misc.get_files(directory, cropped=False)
            misc.is_empty(files)
        case(False, False):
            directory, files = misc.process_user_input(path, single_file=True) if path else misc.get_input(cropped=False)
        case(False, True):
            directory, files = misc.process_user_input(path, single_file=True) if path else misc.get_input(cropped=True)
    return directory, files


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


def main(wizard: bool, file_path: bool, cropped_screens: bool, current_folder: bool, both: bool, view_width: int, view_height: int) -> None:
    '''Main function of the script.'''
    import time
    start_time = time.perf_counter()
    if both:
        show_screenshot_types(current_folder, stdout=True, test=False)
    else:
        directory, files = match_path(current_folder, file_path, cropped_screens)
        print(f'{misc.print_time()}', 'Getting a list of files...')
        start_script(directory, files, wizard, view_width, view_height, stdout=True)
        print(f'{misc.print_time()}', 'The script is finished.')        
    end_time = time.perf_counter()
    finished = end_time - start_time
    print(misc.print_time(), f'finished within: {finished:.2f}')
    misc.script_close(flags=False)
