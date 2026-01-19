'''Contains data, i.e. color of the target pixels.'''

# view targets
def find_central_targets() -> dict:
    '''Contains central targets colors.'''
    targets = {
        'central_target_0' : (229, 165, 90),
        'central_target_1' : (229, 168, 97),
        'central_target_2' : (137, 99, 54),
    }

    return targets

def find_right_targets() -> dict:
    '''Contains right targets colors.'''
    targets = {   
        'right_target_0' : (51, 51, 51),
        'right_target_1' : (31, 31, 31)
    }

    return targets

def find_left_targets() -> dict:
    '''Contains left targets colors.'''
    targets = {
        'left_target_0' : (255, 255, 255),
        'left_target_1' : (153, 153, 153)
    }

    return targets
