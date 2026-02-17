import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wizard', action='store_true', dest='wizard', help='wizard flag')
    parser.add_argument('-v', '--view',   action='store_true', dest='view',   help='view flag')
    parser.add_argument('-x', '--width',  action='store',      dest='width',  help='width value',  type=int, default=1271)
    parser.add_argument('-y', '--height', action='store',      dest='height', help='height value', type=int, default=761)
    parser.add_argument('-f', '--file',   action='store',      dest='path',   help='path value',   type=str, default=None)
    args = parser.parse_args()

    from script import main
    import misc
    print(args)
    match (args.wizard, args.view, args.path is not None):
        case(True,  False, None): main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None)
        case(False, True,  None): main(wizard=False, view_width=args.width, view_height=args.height,  file_path=None)
        case(True,  False, True): main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=args.path)
        case(False, True,  True): main(wizard=False, view_width=args.width, view_height=args.height,  file_path=args.path)        
        case(False, False, None): main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None)
        case(True,  True,  None): misc.close_script_by_duplicated_flags()
