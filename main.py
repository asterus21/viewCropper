'''Main module of the script.

The module handles script arguments to pass them to the main() function.
'''


import argparse

import misc
import script


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wizard',  action='store_true', dest='wizard',    help='flag to process only wizards')
    parser.add_argument('-v', '--view',    action='store_true', dest='view',      help='flag to process only views')
    parser.add_argument('-t', '--type',    action='store_true', dest='type',      help='flag to show types of screenshots')
    parser.add_argument('-d', '--dir',     action='store_true', dest='directory', help='flag to start the script in the current folder')
    parser.add_argument('-c', '--cropped', action='store_true', dest='cropped',   help='flag to process only those screenshots which start with "Cropped_"')
    parser.add_argument('-b', '--both',    action='store_true', dest='both',      help='flag to process both wizards and views')
    parser.add_argument('-x', '--width',   action='store',      dest='width',     help='width value to process views',        type=int, default=1271)
    parser.add_argument('-y', '--height',  action='store',      dest='height',    help='height value to process views',       type=int, default=761)
    parser.add_argument('-f', '--file',    action='store',      dest='path',      help='path value to process a single file', type=str, default=None)
    args = parser.parse_args()

    # matching different flags
    match (args.wizard, args.view, args.path is not None, args.type, args.directory, args.cropped, args.both):
        # script
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, False, False, False, False, False, False): 
            script.main(wizard=True, file_path=args.path, cropped=False, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -w
        # args.wizard=True, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(True, False, False, False, False, False, False): 
            script.main(wizard=True, file_path=args.path, cropped=False, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -v
        # args.wizard=False, args.view=True, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, True, False, False, False, False, False): 
            script.main(wizard=False, file_path=args.path, cropped=False, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -c
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, False, False, False, False, True, False):
            script.main(wizard=True, file_path=args.path, cropped=True, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -w -c
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=True, args.both=False
        case(False, False, False, False, False, True, False):
            script.main(wizard=True, file_path=args.path, cropped=True, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -v -c
        # args.wizard=False, args.view=True, args.path=False, args.type=False, args.directory=False, args.cropped=True, args.both=False
        case(False, True, False, False, False, True, False):
            script.main(wizard=True, file_path=args.path, cropped=True, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -f
        # args.wizard=False, args.view=False, args.path=True, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, False, True, False, False, False, False):
            script.main(wizard=True, file_path=args.path, cropped=False, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -f -w 
        # args.wizard=True, args.view=False, args.path=True, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(True, False, True, False, False, False, False):
            script.main(wizard=True, file_path=args.path, cropped=False, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -f -v 
        # args.wizard=False, args.view=True, args.path=True, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, True, True, False, False, False, False):
            script.main(wizard=False, file_path=args.path, cropped=False, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -f -c
        # args.wizard=False, args.view=False, args.path=True, args.type=False, args.directory=False, args.cropped=True, args.both=False
        case(False, False, True, False, False, True, False):
            script.main(wizard=False, file_path=args.path, cropped=False, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -f -w -c
        # args.wizard=True, args.view=False, args.path=True, args.type=False, args.directory=False, args.cropped=True, args.both=False
        case(True, False, True, False, False, True, False):
            script.main(wizard=False, file_path=args.path, cropped=False, current_folder=False, both=False, view_width=args.width, view_height=args.height)
        # script -f -v -c
        # args.wizard=False, args.view=True, args.path=True, args.type=False, args.directory=False, args.cropped=True, args.both=False
        case(False, True, True, False, False, False, False):
            script.main(wizard=False, file_path=args.path, cropped=False, current_folder=True, both=False, view_width=args.width, view_height=args.height)
        # script -d
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=True, args.cropped=False, args.both=False
        case(False, False, False, False, True, False, False):
            script.main(wizard=True, file_path=args.path, cropped_screens=False, current_folder=True, both=False, view_width=args.width, view_height=args.height)
        # script -d -w
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(True, False, False, False, True, True, False):
            script.main(wizard=True, file_path=args.path, cropped_screens=False, current_folder=True, both=False, view_width=args.width, view_height=args.height)
        # script -d -c
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, False, False, False, True, True, False):
            script.main(wizard=True, file_path=args.path, cropped_screens=True, current_folder=True, both=False, view_width=args.width, view_height=args.height)
        # script -w -d
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(True, False, False, False, True, False, False):
            script.main(wizard=True, file_path=args.path, cropped_screens=False, current_folder=True, both=False, view_width=args.width, view_height=args.height)
        # script -w -d -с
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(True, False, False, False, True, True, False):
            script.main(wizard=True, file_path=args.path, cropped_screens=True, current_folder=True, both=False, view_width=args.width, view_height=args.height)
        # script -v -d
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, True, False, False, True, False, False):
            script.main(wizard=False, file_path=args.path, cropped_screens=False, current_folder=True, both=False, view_width=args.width, view_height=args.height)
        # script -v -d -c
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, True, False, False, True, True, False):
            script.main(wizard=False, file_path=args.path, cropped_screens=True, current_folder=True, both=False, view_width=args.width, view_height=args.height)
        # script -b
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=True
        case(False, False, False, False, False, False, True):
            script.main(wizard=None, current_folder=False, file_path=args.path, cropped_screens=False, both=True, view_width=args.width, view_height=args.height)
        # script -b -d
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=True
        case(False, False, False, False, True, False, True):
            script.main(wizard=None, current_folder=True, file_path=args.path, cropped_screens=False, both=True, view_width=args.width, view_height=args.height)
        # script -t
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, False, False, True, False, False, False):
            script.show_screenshot_types(current_folder=False, stdout=True)
        # script -t -d
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, False, False, True, True, False, False):
            script.show_screenshot_types(current_folder=True, stdout=True)
        # script -w -v
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(True, True, False, False, False, False, False):
            misc.script_close(flags=True)
        # script -t -с
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, False, False, True, True, True, False):
            misc.script_close(flags=True)
        # script -f -d
        # args.wizard=False, args.view=False, args.path=False, args.type=False, args.directory=False, args.cropped=False, args.both=False
        case(False, False, True, False, True, False, False):
            misc.script_close(flags=True)

# TODO: change the -b flag module logic
# TODO: test each script value
