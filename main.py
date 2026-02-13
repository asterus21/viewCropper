import misc
from script import main


if __name__ == '__main__':
    # TODO: add --width, --height, --dry (and -d)
    import sys
    flags = ['-w', '-v', '-x', '-y', '-f', '-h', '-s']
    full_flags = ['--wizard', '--view', '--file', '--help', '--size']
    # start the main script
    if len(sys.argv) == 1:
        directory, files_list = misc.get_input()
        main(
            directory, 
            files_list, 
            wizard=True, 
            view_width=1271, 
            view_height=761
            )
    if len(sys.argv) == 2:
        if sys.argv[1] == '-w':
            directory, files_list = misc.get_input()
            main(
                directory, 
                files_list, 
                wizard=True, 
                view_width=1271, 
                view_height=761
                )
        elif sys.argv[1] == '-v':
            directory, files_list = misc.get_input()
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_width=1271, 
                view_height=761
                )
        elif sys.argv[1] not in flags:
            print("The given flag is not supported!")
            misc.close_script()
    else:
        print("The flag value cannot be empty or less than zero!")
        misc.close_script()
    if len(sys.argv) == 3:
        if sys.argv[1] == '-x' and int(sys.argv[2]) > 0:
            directory, files_list = misc.get_input()
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_width=int(sys.argv[2]), 
                view_height=761
                )
        elif sys.argv[1] == '-y' and int(sys.argv[2]) > 0:
            directory, files_list = misc.get_input()
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_height=int(sys.argv[2]), 
                view_width=1271)
        elif sys.argv[1] == '-f':
            directory, files_list = misc.process_single_input(sys.argv[2])            
            main(
                directory, 
                files_list, 
                wizard=True, 
                view_width=1271, 
                view_height=761
                )
        elif sys.argv[1] not in flags:
            print("The given flag is not supported!")
            misc.close_script()
        else:
            print("The flag value cannot be empty or less than zero!")
            misc.close_script()
    if len(sys.argv) == 5:
        if (sys.argv[1] == '-x' and sys.argv[3] == '-y' and int(sys.argv[2]) > 0 and int(sys.argv[4]) > 0):
            directory, files_list = misc.get_input()           
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_width=int(sys.argv[2]),  
                view_height=int(sys.argv[4])
                )
        elif (sys.argv[1] == '-y' and sys.argv[3] == '-x' and int(sys.argv[2]) > 0 and int(sys.argv[4]) > 0):    
            directory, files_list = misc.get_input()         
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_width=int(sys.argv[4]), 
                view_height=int(sys.argv[2])
                )
        elif (sys.argv[1] == '-x' and sys.argv[3] == '-f' and int(sys.argv[2]) > 0): 
            directory, files_list = misc.process_single_input(sys.argv[4])            
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_width=int(sys.argv[2]), 
                view_height=761
                )
        elif (sys.argv[1] == '-f' and sys.argv[3] == '-x' and int(sys.argv[4]) > 0):
            directory, files_list = misc.process_single_input(sys.argv[2])     
            main(
                directory, 
                files_list, 
                wizard=False,
                view_width=int(sys.argv[4]),
                view_height=761
                )
        elif (sys.argv[1] == '-f' and sys.argv[3] == '-y' and int(sys.argv[4]) > 0):
            directory, files_list = misc.process_single_input(sys.argv[2])
            main(
                directory,
                files_list,
                wizard=False,
                view_width=1271,
                view_height=int(sys.argv[4])
                )
        elif (sys.argv[1] == '-y' and sys.argv[3] == '-f' and int(sys.argv[2]) > 0): 
            directory, files_list = misc.process_single_input(sys.argv[4])            
            main(
                directory,
                files_list,
                wizard=False,
                view_height=int(sys.argv[2]), 
                view_width=1271
                )
        elif sys.argv[1] or sys.argv[3] not in flags:
            print("The given flag is not supported!")
            misc.close_script()
        else:
            print("The flag value cannot be empty or less than zero!")
            misc.close_script()
    if len(sys.argv) == 7:
        if sys.argv[1] == '-x' and sys.argv[3] == '-y' and sys.argv[5] == '-f' and int(sys.argv[2]) > 0 and int(sys.argv[4]) > 0:
            directory, files_list = misc.process_single_input(sys.argv[6])   
            main(
                directory, 
                files_list,
                wizard=False, 
                view_width=int(sys.argv[2]), 
                view_height=int(sys.argv[4])
                )
        elif sys.argv[1] == '-x' and sys.argv[3] == '-f' and sys.argv[5] == '-y' and int(sys.argv[2]) > 0 and int(sys.argv[6]) > 0: 
            directory, files_list = misc.process_single_input(sys.argv[4])
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_height=int(sys.argv[6]), 
                view_width=int(sys.argv[2])
                )
        elif sys.argv[1] == '-y' and sys.argv[3] == '-x' and sys.argv[5] == '-f' and int(sys.argv[2]) > 0 and int(sys.argv[4]) > 0: 
            directory, files_list = misc.process_single_input(sys.argv[-1])   
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_height=int(sys.argv[2]), 
                view_width=int(sys.argv[4])
                )    
        elif sys.argv[1] == '-y' and sys.argv[3] == '-f' and sys.argv[5] == '-x' and int(sys.argv[2]) > 0 and int(sys.argv[6]) > 0: 
            directory, files_list = misc.process_single_input(sys.argv[4])
            main(
                directory,
                files_list,
                wizard=False, 
                view_height=int(sys.argv[2]), 
                view_width=int(sys.argv[6])
                )
        elif sys.argv[1] == '-f' and sys.argv[3] == '-x' and sys.argv[5] == '-y' and int(sys.argv[4]) > 0 and int(sys.argv[-1]) > 0: 
            directory, files_list = misc.process_single_input(sys.argv[2])   
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_height=int(sys.argv[6]), 
                view_width=int(sys.argv[4])
                )
        elif sys.argv[1] == '-f' and sys.argv[3] == '-y' and sys.argv[5] == '-x' and int(sys.argv[4]) > 0 and int(sys.argv[-1]) > 0: 
            directory, files_list = misc.process_single_input(sys.argv[2])   
            main(
                directory, 
                files_list, 
                wizard=False, 
                view_height=int(sys.argv[4]), 
                view_width=int(sys.argv[6])
                )
        elif sys.argv[1] or sys.argv[3] or sys.argv[5] not in flags:
            print("The given flag is not supported!")
            misc.close_script()
        else:
            print("The flag value cannot be empty or less than zero!")
            misc.close_script()

