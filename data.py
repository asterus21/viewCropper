'''Contains data, i.e. color of the target pixels.'''

# view targets
def find_central_targets() -> dict:
    '''Contains central targets colors.'''
    targets = {
        'central_target_0' : (229, 165, 90),
        'central_target_1' : (229, 168, 97),
        'central_target_2' : (137, 99, 54),
        'central_target_3' : (82, 61, 35)
    }

    return targets

def find_right_targets() -> dict:
    '''Contains right targets colors.'''
    targets = {   
        'right_target_0' : (51, 51, 51),
        'right_target_1' : (31, 31, 31),
        'right_target_2' : (19, 19, 19)
    }

    return targets

def find_left_targets() -> dict:
    '''Contains left targets colors.'''
    targets = {
        'left_target_0' : (255, 255, 255),
        'left_target_1' : (153, 153, 153),
        'left_target_2' : (92, 92, 92)
    }

    return targets

# wizard targets
def get_upper_target() -> dict:
    '''Contains upper targets colors.'''
    targets = {
        'upper_0' : (187, 187, 187),
        'upper_1' : (186, 186, 186),
        'upper_2' : (112, 112, 112),
        'upper_3' : (153, 153, 153),
        'upper_4' : (182, 182, 182),
        'upper_5' : (162, 162, 162),
        'upper_6' : (111, 111, 111),
        'upper_7' : (161, 161, 161)
    }

    return targets

def get_upper_neighbors() -> dict:
    '''Contains upper neighbors colors.'''
    targets = {
        'neighbor_0' : (239, 239, 239),
        'neighbor_1' : (143, 143, 143),
        'neighbor_2' : (238, 238, 238)
    }

    return targets

def get_lower_target() -> dict:
    '''Contains lower targets colors.'''
    targets = {
        'lower_0' : (176, 176, 176),
        'lower_1' : (175, 175, 175),
        'lower_2' : (106, 106, 106),
        'lower_3' : (143, 143, 143),
        'lower_4' : (173, 173, 173),
        'lower_5' : (151, 151, 151),
        'lower_6' : (105, 105, 105),
        'lower_7' : (149, 149, 149)
    }

    return targets

def get_lower_neighbors() -> dict:
    '''Contains lower neighbors colors.'''
    targets = {
        'neighbor_0' : (238, 238, 238),
        'neighbor_1' : (143, 143, 143),
        'neighbor_2' : (237, 237, 237),
        'neighbor_3' : (236, 236, 236)
    }

    return targets
