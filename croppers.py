import os
import misc
from PIL import Image


class Croppers:

    def __init__(self, directory: str, files: list, target_pixels: list, view_width: int, view_height: int, wizard: bool, stdout: bool):
        self.directory = directory
        self.files = files
        self.target_pixels = target_pixels
        self.view_width = view_width
        self.view_height = view_height
        self.wizard = wizard
        self.stdout = stdout


    def crop_wizards(self, image, index):
        '''Crops wizards according to the target pixels.'''
        return image.crop((
            self.target_pixels[index][0][0],
            self.target_pixels[index][0][1],
            self.target_pixels[index][1][0] + 1,
            self.target_pixels[index][1][1] + 1
            ))


    def crop_views(self, image, index):
        '''Crops views according to the target pixels.'''
        return image.crop((
            self.target_pixels[index][0] - 12,
            self.target_pixels[index][1] - 15,
            self.view_width,
            self.view_height
            ))


    def crop_corners(self, image, index):
        '''Crops the screenshots according to the target pixels.'''
        if self.wizard:
            return self.crop_wizards(image, index)            
        else: 
            return self.crop_views(image, index)


    def crop_wrapper(self, func) -> None:
        '''Crops the screenshots according to the target pixels.'''
        file_number = 1
        cropped_files = len(misc.get_files(folder=os.getcwd(), cropped_screens=True, all=False))
        for i in range(len(self.files)):
            if not self.target_pixels[i]:
                continue
            image = Image.open(os.path.join(self.directory, self.files[i]))
            try:
                crop = func(image, i)
                if cropped_files:
                    crop.save(f'Cropped_{cropped_files+1}.png')
                    cropped_files += 1
                else:
                    crop.save(f'Cropped_{file_number}.png')
                    file_number += 1
            except Exception as E:
                print(f'{E}: no wizard screenshot or view one is found.')
        if self.stdout:
            print(f'{misc.print_time()}', str(len(self.files)) + ' file(s) processed.')
        return None
