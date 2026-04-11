'''Croppers module.

The module contains a class to crop screenshot according to the found targets.
'''


import os
import misc as misc
from PIL import Image


class Croppers:

    def __init__(self, directory: str, files: list, targets: list, view_width: int, view_height: int, wizard: bool, stdout: bool):
        self.directory   = directory
        self.files       = files
        self.targets     = targets
        self.view_width  = view_width
        self.view_height = view_height
        self.wizard      = wizard
        self.stdout      = stdout


    def crop_wizards(self, image: bytes, index: int) -> object:
        '''Crops wizards according to the target pixels.'''
        return image.crop((
            self.targets[index][0][0],
            self.targets[index][0][1],
            self.targets[index][1][0] + 1,
            self.targets[index][1][1] + 1
            ))


    def crop_views(self, image: bytes, index: int) -> object:
        '''Crops views according to the target pixels.'''
        return image.crop((
            self.targets[index][0] - 12,
            self.targets[index][1] - 15,
            self.view_width,
            self.view_height
            ))


    def crop_corners(self, image: bytes, index: int) -> object:
        '''Crops the screenshots according to the target pixels.'''
        return self.crop_wizards(image, index) if self.wizard else self.crop_views(image, index)


    def crop_screenshots(self, method: object) -> object:
        '''Wrapps the cropping function.'''
        file_number = 1
        cropped_files = len(misc.get_files(folder=os.getcwd(), cropped_screens=True, all_files=False))
        for i in range(len(self.files)):
            image = Image.open(os.path.join(self.directory, self.files[i]))
            try:
                crop = method(image, i)
                if cropped_files:
                    crop.save(f'Cropped_{cropped_files+1}.png')
                    cropped_files += 1
                else:
                    crop.save(f'Cropped_{file_number}.png')
                    file_number += 1
            except Exception as E: print(f'{E}: no wizard screenshot or view one is found.')
        if self.stdout: print(f'{misc.print_time()}', str(len(self.files)) + ' file(s) processed.')
