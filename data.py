'''Data module.

The module contains data, i.e. color of the target pixels given
- as central targets for views called 'RIGHT_TARGETS'
- one pixel to the left called 'LEFT_TARGETS'
- one pixel to the left called 'RIGHT_TARGETS'
- the same goes for wizards where we see
- right targets called 'UPPER_TARGETS'
- one pixel to the right of the target one called 'UPPER_NEIGHBOR_TARGETS'
- left targets called 'LOWER_TARGETS'
- and the same for the neighbor pixel named 'LOWER_NEIGHBOR_TARGETS'
'''

# targets for views
CENTRAL_TARGETS = [
    (229, 165, 90),
    (229, 168, 97),
    (137, 99, 54),
    (82, 61, 35)
    ]

LEFT_TARGETS = [
    (255, 255, 255),
    (153, 153, 153),
    (92, 92, 92)
    ]

RIGHT_TARGETS = [
    (51, 51, 51),
    (31, 31, 31),
    (19, 19, 19)
]

# targets for wizards
UPPER_TARGETS = [
    (187, 187, 187),
    (186, 186, 186),
    (112, 112, 112),
    (182, 182, 182),
    (162, 162, 162),
    (111, 111, 111),
    (161, 161, 161)
]

UPPER_NEIGHBOR_TARGETS = [
    (239, 239, 239),
    (143, 143, 143),
    (238, 238, 238)
]

LOWER_TARGETS = [
    (176, 176, 176),
    (175, 175, 175),
    (106, 106, 106),
    (173, 173, 173),
    (151, 151, 151),
    (105, 105, 105),
    (149, 149, 149)
]

LOWER_NEIGHBOR_TARGETS = [
    (238, 238, 238),
    (143, 143, 143),
    (237, 237, 237),
    (236, 236, 236)
]
