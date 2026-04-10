'''Types module.

The module contains a class to crop get types of the screenshots.
'''

class Types:

    def __init__(self, directory, files):
        self.directory = directory
        self.files = files


    def get_screenshot_types(self) -> dict:
        '''Prints the types of screenshots.'''
        wizards      = self.get_values(keys=None, wizard=True)
        views        = self.get_values(keys=self.get_keys(wizards), wizard=False)
        wizard_types = self.get_types(wizards, wizard=True)
        view_types   = self.get_types(views, wizard=False)
        types        = wizard_types | view_types
        sorts        = dict(sorted(types.items()))
        for key, value in sorts.items(): print(str(key) + ': ' + str(value))
        return sorts


    def get_keys(self, values: dict) -> list:
        '''Gets empty keys to process'''
        return [ key for key in values if not values[key] ]
    
    
    def get_values(self, keys: list, wizard: bool) -> dict:
        '''Gets values for wizards or views.'''
        from classes.targets import Targets
        if wizard: 
            targets_instance = Targets(self.directory, self.files, wizard=True, stdout=False)
            return targets_instance.find_targets(type=True, whole=False)
        else:
            targets_instance = Targets(self.directory, keys, wizard=False, stdout=False)
            return targets_instance.find_targets(type=True, whole=None)       


    def get_types(self, values: dict, wizard: bool) -> dict:
        '''Returns a file type for a screenshot'''
        return ({key: 'wizard' for key, value in values.items() if value} if wizard
                else {key: 'view' for key, value in values.items() if value})
