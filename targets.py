from data import Targets


class Process(Targets):

    def __init__(self, image, height, width):
        Targets.__init__(self)
        self.image  = image
        self.height = height
        self.width  = width


    def get_targets(self, x: int, y: int) -> dict:
        '''Finds target pixels and their neighbours.'''
        targets = dict(
            target = self.image.getpixel((x, y)),
            right  = self.image.getpixel((x + 1, y)),
            down   = self.image.getpixel((x, y + 1)),
            left   = self.image.getpixel((x - 1, y)),
            up     = self.image.getpixel((x, y - 1))
        )
        return targets


    def find_views(self) -> list:
        '''Finds view targets.'''
        coordinates = []
        for x in range(self.width - 1):
            for y in range(self.height - 1):
                t = self.get_targets(x, y)
                if  (
                    t.get('target') in Targets.central and
                    t.get('right')  in Targets.right   and
                    t.get('left')   in Targets.left
                    ):
                    coordinates.append((x, y))
        return coordinates

    
    def find_wizards(self, whole: bool) -> list:
        '''Finds wizard targets.'''
        if whole:
            target_left_coordinates  = []
            target_right_coordinates = []
            for x in range(self.width - 1):
                for y in range(self.height - 1):
                    t = self.get_targets(x, y)
                    if  (
                        t.get('target') in Targets.upper    and
                        t.get('right')  in Targets.neighbor and
                        t.get('down')   in Targets.neighbor
                        ):
                        target_left_coordinates.append((x, y))
                    if  (
                        t.get('target') in Targets.lower    and
                        t.get('left')   in Targets.neighbor and
                        t.get('up')     in Targets.neighbor
                        ):
                        target_right_coordinates.append((x, y))
                coordinates = target_left_coordinates + target_right_coordinates
        else:
            coordinates = []
            for x in range(self.width - 1):
                for y in range(self.height - 1):
                    t = self.get_targets(x, y)
                    if  (
                        t.get('target') in Targets.upper    and
                        t.get('right')  in Targets.neighbor and
                        t.get('down')   in Targets.neighbor
                        ):
                        coordinates.append((x, y))
        return coordinates
