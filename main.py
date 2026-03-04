import argparse
import misc



def start_script_in_current_folder(wizard=True):
    import os
    print(f'{misc.print_time()}', 'Current folder is being used...')
    directory = os.getcwd()            
    files = [file for file in os.listdir(directory) if file.lower().endswith('.png') and not file.startswith('Cropped_')]
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
    parser.add_argument('-w', '--wizard', action='store_true', dest='wizard',    help='wizard flag')
    parser.add_argument('-v', '--view',   action='store_true', dest='view',      help='view flag')
    parser.add_argument('-t', '--type',   action='store_true', dest='type',      help='type flag')
    parser.add_argument('-d', '--dir',    action='store_true', dest='directory', help='directory flag')
    parser.add_argument('-x', '--width',  action='store',      dest='width',     help='width value',  type=int, default=1271)
    parser.add_argument('-y', '--height', action='store',      dest='height',    help='height value', type=int, default=761)
    parser.add_argument('-f', '--file',   action='store',      dest='path',      help='path value',   type=str, default=None)    
    args = parser.parse_args()

    import script
    import os
    # print(args)
    match (args.wizard, args.view, args.path is not None, args.type, args.directory):
        case(True,  False, False, False, False): script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None)
        case(False, True,  False, False, False): script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=None)
        case(True,  False, True, False, False):  script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=args.path)
        case(False, True,  True, False, False):  script.main(wizard=False, view_width=args.width, view_height=args.height,  file_path=args.path)
        case(False, False, _, False, False):     script.main(wizard=True,  view_width=args.width, view_height=args.height,  file_path=None)
        case(True,  True,  _, False, False):     misc.close_script_by_duplicated_flags()        
        case(False, False, _, True, True):       script.print_target_pixels(os.getcwd(), [file for file in os.listdir(os.getcwd()) if file.lower().endswith('.png') and not file.startswith('Cropped_')])
        case(False, False, _, True, False):
            directory, files = misc.get_input()   
            script.print_target_pixels(directory, files)
        case(False, False, _, False, True):      start_script_in_current_folder(wizard=True)
        case(True, False, _, False, True):       start_script_in_current_folder(wizard=True)
        case(False, True, _, False, True):       start_script_in_current_folder(wizard=False)

# TODO: add docstrings and type hints
# TODO: add -b (or --both) flag to process both views and wizards at the same time
# TODO: add -c (or --cropped) flag to process ONLY those screenshots which start with "Cropped_", e.g. to edit already cropped screenshots
# TODO: expand the description for the arguments
