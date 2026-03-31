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


    def crop_corners(self) -> None:
        '''Crops the screenshots according to the target pixels.'''
        file_number = 1
        cropped_files = len(misc.get_files(folder=os.getcwd(), cropped_screens=True, all=False))
        for i in range(len(self.files)):
            if not self.target_pixels[i]: continue
            image = Image.open(os.path.join(self.directory, self.files[i]))
            try:                                    
                if not self.wizard:
                    crop = image.crop((             
                        self.target_pixels[i][0] - 12,   
                        self.target_pixels[i][1] - 15,
                        self.view_width,
                        self.view_height
                        ))                       
                else:                               
                    crop = image.crop((
                        self.target_pixels[i][0][0],     
                        self.target_pixels[i][0][1],     
                        self.target_pixels[i][1][0] + 1, 
                        self.target_pixels[i][1][1] + 1  
                        ))
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


    def crop_wizards(self) -> None:
        '''Crops the screenshots according to the target pixels.'''
        file_number = 1
        cropped_files = len(misc.get_files(folder=os.getcwd(), cropped_screens=True, all=False))
        for i in range(len(self.files)):
            # skips empty coordinates if present
            if not self.target_pixels[i]: continue
            # concatenates a path and file, e.g. 'D:/folder/screenshot_1.png')
            image = Image.open(os.path.join(self.directory, self.files[i]))
            # main logic of the script, i.e. screens cropping
            try:
                if self.stdout:
                    print(f'{misc.print_time()}', 'Processing: ' + self.files[i])
                crop = image.crop((
                    self.target_pixels[i][0][0],
                    self.target_pixels[i][0][1],
                    self.target_pixels[i][1][0] + 1,
                    self.target_pixels[i][1][1] + 1
                    ))
                if cropped_files:
                    crop.save(f'Cropped_{cropped_files+1}.png')
                    cropped_files += 1
                else:
                    crop.save(f'Cropped_{file_number}.png')
                    file_number += 1
            except Exception as E:
                print(f'{E}: no wizard screenshot is found.')
        if self.stdout:
            print(f'{misc.print_time()}', str(len(self.files)) + ' file(s) processed.')
        return None


    def crop_views(self) -> None:
        '''Crops the screenshots according to the target pixels.'''
        file_number = 1
        cropped_files = len(misc.get_files(folder=os.getcwd(), cropped_screens=True, all=False))
        for i in range(len(self.files)):
            # skips empty coordinates if present
            if not self.target_pixels[i]: continue
            # concatenate a path and file, e.g. 'D:/folder/screenshot_1.png')
            image = Image.open(os.path.join(self.directory, self.files[i]))
            # main logic of the script, i.e. screens cropping
            try:
                if self.stdout:
                    print(f'{misc.print_time()}', 'Processing: ' + self.files[i])
                crop = image.crop((
                    self.target_pixels[i][0] - 12,
                    self.target_pixels[i][1] - 15,
                    self.view_width,
                    self.view_height
                    ))
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
