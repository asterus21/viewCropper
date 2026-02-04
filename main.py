'''The script is aimed to crop windows of the PolyAnalyst nodes.'''

import os
from PIL import Image
import data
import misc


# import target colors for views
central_targets       = data.find_central_targets()
right_targets         = data.find_right_targets()
left_targets          = data.find_left_targets()

# import target colors for wizards
target_upper          = data.get_upper_target()
target_upper_neighbor = data.get_upper_neighbors()
target_lower          = data.get_lower_target()
target_lower_neighbor = data.get_lower_neighbors()

# create a list of coordinates for the target pixels
def find_target_pixels(directory: str, files: list, wizard=True) -> list:
    targets = []
    print(f'{misc.print_time()}', 'Getting a list of files...')
    for file in files:
        print(f'{misc.print_time()}', 'Processing: ' + file)
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
        image = Image.open(os.path.join(directory, file)).convert('RGB')
        width, height = image.size
        if wizard:
            t = misc.find_targets_in_wizard(
                    target_upper, 
                    target_upper_neighbor, 
                    target_lower,
                    target_lower_neighbor,
                    width, 
                    height, 
                    image
                    )
        else: 
            t = misc.find_targets_in_view(
                    central_targets, 
                    right_targets, 
                    left_targets, 
                    width, 
                    height, 
                    image
                    )
        # print(targets)
        targets.append(t)
    return targets


def remove_empty_targets(coordinates: list, files: list) -> dict:
    # get a dictionary with file names as keys and their coordinates as values
    s = {
        str(files[i]): coordinates[i] for i in range(0, len(files)) if coordinates[i]
    }
    # print(s)
    return s


def edit_coordinates(coordinates: dict, wizard=True) -> list:
    # fetch only the first target in case there are several ones
    # print(coordinates)
    if not wizard:
        coordinates_list = [
            item[0] for item in coordinates.values() if item
        ]
    else:
        coordinates_list = [
            (item[0], item[-1]) for item in coordinates.values() if item
        ]
    # print(coordinates_list)
    return coordinates_list


def get_new_list_of_files(files: dict) -> list:
    # fetch only the keys of the dictionary, i.e. files names
    # print(files.keys())
    return(list(files.keys()))


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


def main(directory, files, wizard, view_width=1271, view_height=761):    
    # find target pixels
    f = find_target_pixels(directory, files, wizard)

    # remove empty coordinates
    r = remove_empty_targets(f, files)

    # get a new list of files, i.e. remove those where there are no targets
    l = get_new_list_of_files(r)

    # edit the list, i.e. get only the first occurence
    e = edit_coordinates(r, wizard)

    # show that the script is finished
    crop_corners(directory, l, e, wizard, view_width, view_height)

    # close the script
    print(f'{misc.print_time()}', 'The script is finished.')
    misc.close_script()

if __name__ == '__main__':  
    import sys

    # get the user's input
    directory, files_list = misc.get_input()

    # start the main script    
    if len(sys.argv) > 1:
        print(sys.argv[:])
        if  sys.argv[1] == '-w':
            main(directory, files_list, wizard=True)
        elif sys.argv[1] == '-v':
            main(directory, files_list, wizard=False)
        elif sys.argv[1] == '-x':
            main(directory, files_list, wizard=False, view_width=int(sys.argv[-1]))
        elif sys.argv[1] == '-y':
            main(directory, files_list, wizard=False, view_height=int(sys.argv[-1]))
        elif sys.argv[1] == '-x' and sys.argv[3] == '-y':            
            main(directory, files_list, wizard=False, view_width=int(sys.argv[2]), view_height=int(sys.argv[4]))    
    else:
        main(directory, files_list, wizard=True)
