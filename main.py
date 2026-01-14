'''The script is aimed to crop wizard windows of the PolyAnalyst nodes.'''

import os
from PIL import Image
import data
import misc

# import target colors
target = data.find_targets()

# find target pixels and their neighbours
def get_targets(image, x: int, y: int) -> dict:
    targets = dict(
        target_0 = image.getpixel((x, y)),
        target_1 = image.getpixel((x + 1, y)),
        target_2 = image.getpixel((x - 1, y))
    )
    return targets

# create a list of coordinates for the target pixels
def find_target_pixels(directory: str, files: list) -> list:
    targets = []
    print(f'{misc.print_time()}', 'Getting a list of files...')
    print(f'{misc.print_time()}', 'There ' + str(len(files)) + ' file(s) found that match the pattern.')
    for file in files:
        print(f'{misc.print_time()}', 'Processing: ' + file)
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
        image = Image.open(os.path.join(directory, file)).convert('RGB')
        width, height = image.size
        coordinates = []
        for x in range(width - 1):
            for y in range(height - 1):
                t = get_targets(image, x, y)
                if (
                    t.get('target_0')     == target.get('target_0')
                    and t.get('target_1') == target.get('target_1')
                    and t.get('target_2') == target.get('target_2')
                ): coordinates.append((x, y))
        targets.append(coordinates)
    # print(targets)
    return targets


def remove_empty_targets(coordinates: list, files: list) -> dict:
    # get a dictionary with file names as keys and their coordinates as values
    s = {
        str(files[i]): coordinates[i] for i in range(0, len(files)) if coordinates[i]
    }
    print(s)
    return s


def edit_coordinates_list_as_dictionary(coordinates: dict) -> list:
    # fetch only the first and the last targets in case there are several ones
    coordinates_list = [
        item[0] for item in coordinates.values() if item
    ]
    # print(coordinates_list)
    return coordinates_list


def get_new_list_of_files(files: dict) -> list:
    # fetch only the keys of the dictionary, i.e. files names
    # print(files.keys())
    return(list(files.keys()))


# main logic of the script, i.e. image cropping
def crop_corners(directory: str, files: list, target_pixels: list) -> None:
    file_number = 1
    for i in range(len(files)):
        # skip empty coordinates
        if not target_pixels[i]: continue
        # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
        image = Image.open(os.path.join(directory, files[i]))
        # main logic of the script, i.e. screens cropping
        crop = image.crop((
            target_pixels[i][0] - 12,
            target_pixels[i][1] - 15,
            1271,
            761
            ))
        crop.save(f'Cropped_{file_number}.png')
        file_number += 1


def main(directory, files):
    # find target pixels
    f = find_target_pixels(directory, files)
    # remove empty coordinates
    r = remove_empty_targets(f, files)
    # get a new list of files, i.e. remove those where there are no targets
    l = get_new_list_of_files(r)
    # edit the list, i.e. get only the first occurence
    e = edit_coordinates_list_as_dictionary(r)
    # show that the script is finished
    crop_corners(directory, l, e)
    print(f'{misc.print_time()}', 'The script is finished.')
    # close the script
    misc.close_script()


if __name__ == '__main__':
    # get the user's input
    directory, files_list = misc.get_input()
    # start the main script
    main(directory, files_list)
