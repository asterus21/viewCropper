"""data module

This module contains data, i.e. color of the target pixels given
- as central targets for views
- one pixel to the right called 'right_targets'
- one pixel to the left called 'left_targets'
- the same is for wizards where go
- one pixel to the right of the target one
- one pixel below the target one
- and the same for the target pixel on the bottom left cornen
"""

# view targets
central_targets = [
        (229, 165, 90),
        (229, 168, 97),
        (137, 99, 54),
        (82, 61, 35),
        (242, 210, 173)
    ]

right_targets = [
        (51, 51, 51),
        (31, 31, 31),
        (19, 19, 19),
        (153, 153, 153)
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
    # (153, 153, 153),
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

lower_targets = [
    (176, 176, 176),
    (175, 175, 175),
    (106, 106, 106),
    # (143, 143, 143),
    (173, 173, 173),
    (151, 151, 151),
    (105, 105, 105),
    (149, 149, 149)
]

lower_neighbor_targets = [
    (238, 238, 238),
    (143, 143, 143),
    (237, 237, 237),
    (236, 236, 236)
]
