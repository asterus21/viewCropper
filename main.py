import argparse
import misc


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wizard',  action='store_true', dest='wizard',    help='wizard flag')
    parser.add_argument('-v', '--view',    action='store_true', dest='view',      help='view flag')
    parser.add_argument('-t', '--type',    action='store_true', dest='type',      help='type flag')
    parser.add_argument('-d', '--dir',     action='store_true', dest='directory', help='directory flag')
    parser.add_argument('-c', '--cropped', action='store_true', dest='cropped',   help='name flag')
    parser.add_argument('-b', '--both',    action='store_true', dest='both',      help='process both wizards and views')
    parser.add_argument('-x', '--width',   action='store',      dest='width',     help='width value',  type=int, default=1271)
    parser.add_argument('-y', '--height',  action='store',      dest='height',    help='height value', type=int, default=761)
    parser.add_argument('-f', '--file',    action='store',      dest='path',      help='path value',   type=str, default=None)
    args = parser.parse_args()

    import script
    import os
    match (args.wizard, args.view, args.path is not None, args.type, args.directory, args.cropped, args.both):
        # script
        case(False, False, False, False, False, False, False): script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None, cropped=False, current_folder=False)
        # script -w
        case(True,  False, False, False, False, False, False): script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None, cropped=False, current_folder=False)
        # script -v
        case(False,  True, False, False, False, False, False): script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=None, cropped=False, current_folder=False)
        # script -w -v
        case(True, True,  False, False, False, False, False):  misc.script_close(True)
        # script -c
        case(False, False, False, False, False, True, False):  script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None, cropped=True, current_folder=False)
        # script -w -c
        case(True, False, False, False, False, True, False):   script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None, cropped=True, current_folder=False)
        # script -v-c
        case(False, True, False, False, False, True, False):   script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None, cropped=True, current_folder=False)
        # script -f
        case(False, False, True, False, False, False, False):  script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=args.path, cropped=False, current_folder=False)
        # script -w -f
        case(True,  False, True, False, False, False, False):  script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=args.path, cropped=False, current_folder=False)
        # script -v -f 
        case(False, True, True, False, False, False, False):   script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=args.path, cropped=False, current_folder=False)
        # script -c -f
        case(True, False, True, False, False, True, False):    script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=args.path, cropped=False, current_folder=False)
        # script -d
        case(False, False, False, False, True, False, False):  script.main(wizard=True, file_path=False, cropped=False, current_folder=True, view_width=args.width, view_height=args.height)
        # script -d -c
        case(False, False, False, False, True, True, False):   script.main(wizard=True, file_path=False, cropped=True, current_folder=True, view_width=args.width, view_height=args.height)
        # script -t
        case(False, False, False, True, False, False, False):  misc.one_liner_script()
        # script -t -d
        case(False, False, False, True, True, False, False):   script.print_target_pixels(os.getcwd(), misc.get_files(os.getcwd(), cropped=False))
        # script -t -с
        case(False, False, False, True, True, True, False):    script.print_target_pixels(os.getcwd(), misc.get_files(os.getcwd(), cropped=True))
        # script -w -d
        case(True, False, False, False, True, False, False):   script.main(wizard=True, file_path=False, cropped=False, current_folder=True, view_width=args.width, view_height=args.height)
        # script -w -d -с
        case(True, False, False, False, True, True, False):    script.main(wizard=True, file_path=False, cropped=True, current_folder=True, view_width=args.width, view_height=args.height)
        # script -v -d
        case(False, True, False, False, True, False, False):   script.main(wizard=False, file_path=False, cropped=False, current_folder=True, view_width=args.width, view_height=args.height)
        # script -v -d -c
        case(False, True, False, False, True, True, False):    script.main(wizard=False, file_path=False, cropped=True, current_folder=True, view_width=args.width, view_height=args.height)
        # script -f -d
        case(False, False, True, False, True, False, False):   misc.script_close(True)
        # script -b
        case(False, False, False, False, False, False, True):  script.start_script_for_both_wizards_and_views(cropped=False, file_path=None)


# TODO: split the find_targets() function into two and check for a different type of screenshots if there are no wizards or views found
# TODO: add -b (or --both) flag to process both views and wizards at the same time
# TODO: add docstrings and type hints
# TODO: expand the description for the arguments
# handle the script -w -f /path/to_file.png file not found exception
