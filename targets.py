from data import Data


class Process(Data):

    def __init__(self, image, height, width):
        Data.__init__(self)
        self.image  = image
        self.height = height
        self.width  = width


    def get_Data(self, x: int, y: int) -> dict:
        '''Finds target pixels and their neighbours.'''
        Data = dict(
            target = self.image.getpixel((x, y)),
            right  = self.image.getpixel((x + 1, y)),
            down   = self.image.getpixel((x, y + 1)),
            left   = self.image.getpixel((x - 1, y)),
            up     = self.image.getpixel((x, y - 1))
        )
        return Data


    def find_views(self) -> list:
        '''Finds view Data.'''
        coordinates = []
        for x in range(self.width - 1):
            for y in range(self.height - 1):
                t = self.get_Data(x, y)
                if  (
                    t.get('target') in Data.central and
                    t.get('right')  in Data.right   and
                    t.get('left')   in Data.left
                    ):
                    coordinates.append((x, y))
        return coordinates

    
    def find_wizards(self, whole: bool) -> list:
        '''Finds wizard Data.'''
        if whole:
            target_left_coordinates  = []
            target_right_coordinates = []
            for x in range(self.width - 1):
                for y in range(self.height - 1):
                    t = self.get_Data(x, y)
                    if  (
                        t.get('target') in Data.upper    and
                        t.get('right')  in Data.neighbor and
                        t.get('down')   in Data.neighbor
                        ):
                        target_left_coordinates.append((x, y))
                    if  (
                        t.get('target') in Data.lower    and
                        t.get('left')   in Data.neighbor and
                        t.get('up')     in Data.neighbor
                        ):
                        target_right_coordinates.append((x, y))
                coordinates = target_left_coordinates + target_right_coordinates
        else:
            coordinates = []
            for x in range(self.width - 1):
                for y in range(self.height - 1):
                    t = self.get_Data(x, y)
                    if  (
                        t.get('target') in Data.upper    and
                        t.get('right')  in Data.neighbor and
                        t.get('down')   in Data.neighbor
                        ):
                        coordinates.append((x, y))
        return coordinates
