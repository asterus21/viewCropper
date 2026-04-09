class Types:

    def __init__(self, directory, files):
        self.directory = directory
        self.files = files


    def get_screenshot_types(self) -> tuple:
        '''Returns the types of screenshots.'''
        values = self.get_types(self.get_values())
        for key, value in values.items(): print(str(key) + ': ' + str(value))


    def get_keys(self, values: dict) -> list:
        '''Gets empty keys to process'''
        keys = [
            key for key in values if not values[key]
        ]
        return keys


    def get_values(self) -> tuple:
        '''Gets values for wizards or views.'''
        from classes.targets import Targets
        targets_instance = Targets(self.directory, self.files, wizard=True, stdout=False)
        coordinates = targets_instance.find_target_types()
        return coordinates


    def get_types(self, values: dict) -> dict:
        '''Returns a file type for a screenshot'''
        types = {
                key: 'wizard' if value else 'view' for key, value in values.items() 
            }
        return types
