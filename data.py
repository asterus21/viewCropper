'''Contains data, i.e. color of the target pixels.'''

# view targets
central_targets = [
        (229, 165, 90),
        (229, 168, 97),
        (137, 99, 54),
        (82, 61, 35)
    ]

right_targets = [
        (51, 51, 51),
        (31, 31, 31),
        (19, 19, 19)
]

left_targets = [
        (255, 255, 255),
        (153, 153, 153),
        (92, 92, 92)
    ]

# wizard targets
upper_targets = [
    (187, 187, 187),
    (186, 186, 186),
    (112, 112, 112),
    (153, 153, 153),
    (182, 182, 182),
    (162, 162, 162),
    (111, 111, 111),
    (161, 161, 161)
]


upper_neighbor_targets = [
    (239, 239, 239),
    (143, 143, 143),
    (238, 238, 238)
]


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
