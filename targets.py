from data import Targets


class Process(Targets):

    def __init__(self, image, height, width):
        super().__init__()
        self.image  = image
        self.height = height
        self.width  = width


    def get_targets(self, image, x: int, y: int) -> dict:
        '''Finds target pixels and their neighbours.'''
        targets = dict(
            target = image.getpixel((x, y)),
            right  = image.getpixel((x + 1, y)),
            down   = image.getpixel((x, y + 1)),
            left   = image.getpixel((x - 1, y)),
            up     = image.getpixel((x, y - 1))
        )
        return targets

    
    def find_wizards(self, image: bytes, height: int, width: int, whole: bool) -> list:
        '''Finds wizard targets.'''
        if whole:
            target_left_coordinates  = []
            target_right_coordinates = []
            for x in range(width - 1):
                for y in range(height - 1):
                    t = self.get_targets(image, x, y)
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
            for x in range(width - 1):
                for y in range(height - 1):
                    t = self.get_targets(image, x, y)
                    if  (
                        t.get('target') in Targets.upper    and
                        t.get('right')  in Targets.neighbor and
                        t.get('down')   in Targets.neighbor
                        ):
                        coordinates.append((x, y))
        return coordinates


    def find_views(self, image: bytes, height: int, width: int):
        '''Finds view targets.'''
        coordinates = []
        for x in range(width - 1):
            for y in range(height - 1):
                t = self.get_targets(image, x, y)
                if  (
                    t.get('target') in Targets.central and
                    t.get('right')  in Targets.right   and
                    t.get('left')   in Targets.left
                    ):
                    coordinates.append((x, y))
        return coordinates
