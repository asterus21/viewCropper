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
    parser.add_argument('-s', '--strict',  action='store_true', dest='strict',    help='flag to process only those screenshots which start with "Screenshot_"')
    parser.add_argument('-x', '--width',   action='store',      dest='width',     help='width value to process views',        type=int, default=1271)
    parser.add_argument('-y', '--height',  action='store',      dest='height',    help='height value to process views',       type=int, default=761)
    parser.add_argument('-f', '--file',    action='store',      dest='path',      help='path value to process a single file', type=str, default=None)
    args = parser.parse_args()

    # from Claude:
    # for the use of -x and -y flags without -v
    if (args.width != 1271 or args.height != 761) and not args.view and not args.wizard:
        args.view = True
    else:
        pass
    match (args.wizard, args.view, args.path is not None, args.type, args.directory, args.cropped, args.both, args.strict):
        # script
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, False, False, False, False):
            script.main(
                wizard=True,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -w
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, False, False, False, False, False, False, False):
            script.main(
                wizard=True,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -v
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, True, False, False, False, False, False, False):
            script.main(
                wizard=False,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, False, True, False, False):
            script.main(
                wizard=True,
                cropped_screens=True,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -s
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, False, False, False, True):
            script.main(
                wizard=True,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=False,
				strict=True,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -s -w
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, False, False, False, False, False, False, True):
            script.main(
                wizard=True,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=False,
				strict=True,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -w -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, False, False, False, False, True, False, False):
            script.main(
                wizard=True,
                cropped_screens=True,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -v -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, True, False, False, False, True, False, False):
            script.main(
                wizard=False,
                cropped_screens=True,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -f
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, True, False, False, False, False, False):
            script.main(
                wizard=True,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -f -w
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, False, True, False, False, False, False, False):
            script.main(
                wizard=True,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -f -v
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, True, True, False, False, False, False, False):
            script.main(
                wizard=False,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -d
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, True, False, False, False):
            script.main(
                wizard=True,
                cropped_screens=False,
                current_folder=True,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -d -w
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, False, False, False, True, False, False, False):
            script.main(
                wizard=True,
                cropped_screens=False,
                current_folder=True,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -d -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, True, True, False, False):
            script.main(
                wizard=True,
                cropped_screens=True,
                current_folder=True,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -d -с -w
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, False, False, False, True, True, False, False):
            script.main(
                wizard=True,
                cropped_screens=True,
                current_folder=True,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -v -d
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, True, False, False, True, False, False, False):
            script.main(
                wizard=False,
                cropped_screens=False,
                current_folder=True,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -v -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, True, False, False, True, True, False, False):
            script.main(
                wizard=False,
                cropped_screens=True,
                current_folder=True,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -v -d -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, True, False, False, True, True, False, False):
            script.main(
                wizard=False,
                cropped_screens=True,
                current_folder=True,
                both=False,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -b
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, False, False, True, False):
            script.main(
                wizard=None,
                cropped_screens=False,
                current_folder=False,
                both=True,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -b -d
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, True, False, True, False):
            script.main(
                wizard=None,
                cropped_screens=False,
                current_folder=True,
                both=True,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -b -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, False, True, True, False):
            script.main(
                wizard=None,
                cropped_screens=True,
                current_folder=False,
                both=True,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -b -s
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, False, False, True, True):
            script.main(
                wizard=None,
                cropped_screens=False,
                current_folder=False,
                both=True,
                type=False,
				strict=True,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -b -d -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, True, True, True, False):
            script.main(
                wizard=None,
                cropped_screens=True,
                current_folder=True,
                both=True,
                type=False,
				strict=False,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -b -s -d
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, True, False, True, True):
            script.main(
                wizard=None,
                cropped_screens=False,
                current_folder=True,
                both=True,
                type=False,
				strict=True,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -t
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, True, False, False, False, False):
            script.main(
                wizard=False,
                cropped_screens=False,
                current_folder=False,
                both=False,
                type=True,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -t -с
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, True, False, True, False, False):
            script.main(
                wizard=False,
                cropped_screens=True,
                current_folder=False,
                both=False,
                type=True,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -t -d
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, True, True, False, False, False):
            script.main(
                wizard=False,
                cropped_screens=False,
                current_folder=True,
                both=False,
                type=True,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -t -d -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, True, True, True, False, False):
            script.main(
                wizard=False,
                cropped_screens=True,
                current_folder=True,
                both=False,
                type=True,
                file_path=args.path,
                view_width=args.width,
                view_height=args.height
                )
        # script -w -v
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, True, False, False, False, False, False, False):
            misc.script_close(flags=True)
        # script -f -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, True, False, False, True, False, False):
            misc.script_close(flags=True)
        # script -s -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, False, True, False, True):
            misc.script_close(flags=True)
        # script -f -d
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, True, False, True, False, False, False):
            misc.script_close(flags=True)
        # script -b -s -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, False, False, True, True, True):
            misc.script_close(flags=True)
        # script -f -d -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, True, False, True, True, False, False):
            misc.script_close(flags=True)
        # script -f -t -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, True, True, False, True, False, False):
            misc.script_close(flags=True)
        # script -f -w -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, False, True, False, False, True, False, False):
            misc.script_close(flags=True)
        # script -f -w -c -d
        # wizard, view, path, type, directory, cropped, both, strict
        case(True, False, True, False, True, True, False, False):
            misc.script_close(flags=True)
        # script -f -v -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, True, True, False, False, True, False, False):
            misc.script_close(flags=True)
        # script -f -v -c -d
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, True, True, False, True, True, False, False):
            misc.script_close(flags=True)
        # script -t -d -b
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, True, True, False, True, False):
            misc.script_close(flags=True)
        # script -t -d -b -c
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, True, True, True, True, False):
            misc.script_close(flags=True)
        # script -t -b
        # wizard, view, path, type, directory, cropped, both, strict
        case(False, False, False, True, False, True, True, False):
            misc.script_close(flags=True)

# TODO: use the --strict flag by default
# TODO: if given, then process all screenshots
# TODO: or name it as -a or --all
# TODO: then process views only
# TODO: as it is faster
# TODO: try to use a simplified mode of wizards searching
# TODO: try to use dictionary comprehensions when cropping screenshots
# TODO: test each script value
# TODO: use classes
