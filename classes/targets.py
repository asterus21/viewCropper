'''Targets module.

The module contains a class to process target pixels.
'''

import os
from PIL import Image

import misc

from classes.process import Process


class Targets:
    
    def __init__(self, directory, files, wizard, stdout):
        self.directory = directory
        self.files = files
        self.wizard = wizard
        self.stdout = stdout
  

    def find_targets(self) -> tuple:
        '''Calls the processing function and removes not processed screenshots.'''
        targets = []
        for file in self.files:
            if self.stdout:
                print(f'{misc.print_time()}', 'Processing: ' + file)
                self.process_targets(file, targets)
            else: self.process_targets(file, targets)
        return self.remove_empty_values(targets)


    def remove_empty_values(self, values: list) -> tuple:
        '''Removes empty values in a list of found targets.'''
        coordinates = {
            self.files[i]: values[i] for i in range(0, len(self.files))
            if values[i]
        }
        return coordinates, list(coordinates.keys())


    def find_target_types(self) -> dict:
        '''Calls the processing function and removes not processed screenshots.'''
        targets = []
        for file in self.files:
            if self.stdout:
                print(f'{misc.print_time()}', 'Processing: ' + file)
                self.process_targets(file, targets)
            else: self.process_targets(file, targets)
        return self.return_all_values(targets)
    

    def return_all_values(self, values: list) -> dict:
        '''Removes empty values in a list of found targets.'''
        return { self.files[i]: values[i] for i in range(0, len(self.files)) }


    def process_targets(self, file: str, targets_list: list) -> list:
        '''Finds targets for both wizards and views.'''
        image = Image.open(os.path.join(self.directory, file)).convert('RGB')
        width, height = image.size
        process = Process(image, height, width)
        try:
            if self.wizard: targets_list.append(process.find_wizards(whole=True))
            else: targets_list.append(process.find_views())
        except:
            print(misc.print_time(), (f'File {file} not found!'))
            misc.script_close(flags=False)
        return targets_list


    def get_coordinates(self, coordinates: dict) -> list:
        '''Filters out the target pixels.'''
        return ( [(item[0], item[-1]) for item in coordinates.values() if item] if self.wizard
                else [item[0] for item in coordinates.values() if item] )
