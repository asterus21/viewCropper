import argparse
import misc


def start_script_in_current_folder(wizard=True):
    print(f'{misc.print_time()}', 'Current folder is being used...')
    import os
    directory = os.getcwd()
    files = misc.get_files(directory, cropped=True)
    targets = script.find_target_pixels(directory, files, wizard)
    non_empty_files = script.get_new_list_of_files(targets)
    edited_coordinates = script.edit_coordinates(targets, wizard)    
    script.crop_corners(
        directory, 
        non_empty_files, 
        edited_coordinates, 
        wizard, 
        view_width=args.width, 
        view_height=args.height
        )
    print(f'{misc.print_time()}', 'The script is finished.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wizard',  action='store_true', dest='wizard',    help='wizard flag')
    parser.add_argument('-v', '--view',    action='store_true', dest='view',      help='view flag')
    parser.add_argument('-t', '--type',    action='store_true', dest='type',      help='type flag')
    parser.add_argument('-d', '--dir',     action='store_true', dest='directory', help='directory flag')
    # parser.add_argument('-c', '--cropped', action='store_true', dest='cropped',   help='name flag')
    parser.add_argument('-x', '--width',   action='store',      dest='width',     help='width value',  type=int, default=1271)
    parser.add_argument('-y', '--height',  action='store',      dest='height',    help='height value', type=int, default=761)
    parser.add_argument('-f', '--file',    action='store',      dest='path',      help='path value',   type=str, default=None)
    args = parser.parse_args()

    import script
    import os
    match (args.wizard, args.view, args.path is not None, args.type, args.directory):
        # script
        case(False, False, False, False, False):  script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None)
        # script -w
        case(True,  False, False, False, False):  script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None)
        # script -v
        case(False,  True, False, False, False):  script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=None)
        # script -f
        case(False, False, True, False, False):   script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=args.path)
        # script -w -f
        case(True,  False, True, False, False):   script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=args.path)
        # script -v -f 
        case(False, True, True, False, False):    script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=args.path)
        # script -w -v
        case(True, True,  False, False, False):   misc.close_script_by_conflicting_flags()
        # script -t
        case(False, False, False, True, False):   misc.one_liner_script()
        # script -t -d
        case(False, False, False, True, True):    script.print_target_pixels(os.getcwd(), misc.get_files(os.getcwd(), cropped=True))
        # script -d
        case(False, False, False, False, True):   start_script_in_current_folder(wizard=True)
        # script -w -d
        case(True, False, False, False, True):    start_script_in_current_folder(wizard=True)
        # script -v -d
        case(False, True, False, False, True):    start_script_in_current_folder(wizard=False)
        # script -f -d
        case(False, False, True, False, True):    misc.close_script_by_conflicting_flags()

# TODO: split the find_targets() function into two and check for a different type of screenshots if there are no wizards or views found
# TODO: add -c (or --cropped) flag to process ONLY those screenshots which start with "Cropped_", e.g. to edit already cropped screenshots
# TODO: add -b (or --both) flag to process both views and wizards at the same time
# TODO: add docstrings and type hints
# TODO: expand the description for the arguments


