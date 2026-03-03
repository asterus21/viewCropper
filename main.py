import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wizard', action='store_true', dest='wizard', help='wizard flag')
    parser.add_argument('-v', '--view',   action='store_true', dest='view',   help='view flag')
    parser.add_argument('-t', '--type',   action='store_true', dest='type',   help='type flag')
    parser.add_argument('-x', '--width',  action='store',      dest='width',  help='width value',  type=int, default=1271)
    parser.add_argument('-y', '--height', action='store',      dest='height', help='height value', type=int, default=761)
    parser.add_argument('-f', '--file',   action='store',      dest='path',   help='path value',   type=str, default=None)    
    args = parser.parse_args()

    import script
    import misc
    # print(args)
    match (args.wizard, args.view, args.path is not None, args.type):
        case(True,  False, False, False): script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None)
        case(False, True,  False, False): script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=None)
        case(True,  False, True, False):  script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=args.path)
        case(False, True,  True, False):  script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=args.path)
        case(False, False, _, False):     script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None)
        case(True,  True,  _, False):     misc.close_script_by_duplicated_flags()
        case(_, _, _, True):              
            directory, files = misc.get_input()
            targets = script.print_target_pixels(directory, files)
            script.get_type_of_image(targets)


# TODO: add docstrings and type hints
# TODO: add -s (or --size) flag to show the size of all screens STARTING from the target pixel
# TODO: add -a (or --all) flag for the use of -s and -t together
# TODO: add -d (or --dir) flag for not to specify the directory path
# TODO: add -b (or --both) flag to process both views and wizards at the same time
# TODO: add -c (or --cropped) flag to process ONLY those screenshots which start with "Cropped_", e.g. to edit already cropped screenshots
# TODO: expand the description for the arguments
