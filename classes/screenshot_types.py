'''Types module.

The module contains a class to crop get types of the screenshots.
'''

class Types:

    def __init__(self, directory, files):
        self.directory = directory
        self.files = files


    def get_screenshot_types(self) -> None:
        '''Prints the types of screenshots.'''
        values = self.get_types(self.get_values())
        for key, value in values.items(): print(str(key) + ': ' + str(value))
        return None


    def get_keys(self, values: dict) -> list:
        '''Gets empty keys to process'''
        return [ key for key in values if not values[key] ]


    def get_values(self) -> dict:
        '''Gets values for wizards or views.'''
        from classes.targets import Targets
        targets_instance = Targets(self.directory, self.files, wizard=True, stdout=False)
        return targets_instance.find_target_types()


    def get_types(self, values: dict) -> dict:
        '''Returns a file type for a screenshot'''
        return { key: 'wizard' if value else 'view' for key, value in values.items() }
