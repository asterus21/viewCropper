'''Test module.

The module performs unit tests.
'''

import subprocess


valid_commands = [
    'py main.py -h',                                                  # show help
    'py main.py',                                                     # default script, i.e. processing wizards only    
    'py main.py -w',                                                  # processing wizards
    'py main.py -v',                                                  # processing views
    'py main.py -a',                                                  # processing wizards of any name except Cropped_
    'py main.py -c',                                                  # processing cropped wizards implicitly
    'py main.py -d',                                                  # processing wizards in the current folder implicitly
    'py main.py -b',                                                  # processing both wizards and views
    'py main.py -x 100',                                              # processing views with the width value of 100
    'py main.py -y 100',                                              # processing views with the height value of 100
    'py main.py -x 100 -y 100',                                       # processing views with the width and height values of 100
    'py main.py -y 200 -x 200',                                       # processing views with the height and width values of 100
    'py main.py -w -c',                                               # processing cropped wizards explicitly
    # 'py main.py -v -c',                                             # processing cropped views
    'py main.py -f D:/py/viewCropper/Screenshot_1.png',               # processing a wizard
    'py main.py -x 100 -f D:/py/viewCropper/Screenshot_2.png',        # processing a view with an X-coordinate first
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -x 100',        # processing a view with an X-coordinate last
    'py main.py -y 100 -f D:/py/viewCropper/Screenshot_2.png',        # processing a view with a Y-coordinate first
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -y 100',        # processing a view with a Y-coordinate last
    'py main.py -x 200 -y 200 -f D:/py/viewCropper/Screenshot_2.png', # processing a view with an X-coordinate and a Y-coordinate first
    'py main.py -x 200 -f D:/py/viewCropper/Screenshot_2.png -y 200', # processing a view with an X-coordinate first and a Y-coordinate last
    'py main.py -y 200 -f D:/py/viewCropper/Screenshot_2.png -x 200', # processing a view with a Y-coordinate first and an X-coordinate last
    'py main.py -y 200 -x 200 -f D:/py/viewCropper/Screenshot_2.png', # processing a view with a Y-coordinate and an X-coordinate first
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -x 200 -y 200', # processing a view with an X-coordinate and a Y-coordinate last where X is before Y
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -y 200 -x 200', # processing a view with an X-coordinate and a Y-coordinate last where Y is before
    'py main.py -d -w',                                               # processing wizards in the current folder explicitly
    'py main.py -d -v',                                               # processing views in the current folder
    'py main.py -d -c',                                               # processing wizards in the current folder implicitly starting with Cropped_
    'py main.py -d -w -c',                                            # processing wizards in the current folder starting with Cropped_ explicitly
    'py main.py -v -d -a',                                            # processing views in the current folder of any name except Cropped_
    'py main.py -w -d -a',                                            # processing wizards in the current folder of any name except Cropped_
    'py main.py -v -d -c',                                            # processing views in the current folder starting with Cropped_ 
    'py main.py -b -d',                                               # processing both wizards and views in the current folder 
    'py main.py -b -c',                                               # processing both wizards and views starting with Cropped_
    'py main.py -b -d -c',                                            # processing both wizards and views in the current folder starting with Cropped_
    'py main.py -t',                                                  # processing types
    'py main.py -t -c',                                               # processing types starting with Cropped_
    'py main.py -t -a',                                               # processing types of any name except Cropped_
    'py main.py -t -d',                                               # processing types in the current folder
    'py main.py -t -d -c',                                            # processing types in the current folder starting with Cropped_
    'py main.py -t -d -a'                                             # processing types in the current folder of any name except Cropped_
]


not_valid_commands = [
    'py main.py -x 100 -a 100',
    'py main.py -y 100 -a 100',
    'py main.py -a 100 -b 100',
    'py main.py -a -b'  
    'py main.py -w -v',
    'py main.py -f -c',
    'py main.py -a -c',
    'py main.py -f -d',
    'py main.py -b -a -c',
    'py main.py -f -d -c',
    'py main.py -f -t -c',
    'py main.py -f -w -c',
    'py main.py -f -w -c -d',
    'py main.py -f -v -c',
    'py main.py -f -v -c -d',
    'py main.py -t -d -b',
    'py main.py -t -d -b -c',
    'py main.py -t -d -c -a',
    'py main.py -t -b'
]


def test_start(commands: list) -> tuple:
    import os
    script_number = 0
    from datetime import datetime
    for script in commands:
        print(f'Starting "{ script }":')
        start_time = datetime.now()
        process = subprocess.Popen(
            script,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text   = True
            )
        stdout, stderr = process.communicate(input='\n')
        end_time = datetime.now()
        time_difference = end_time - start_time
        print(f'The test finished within {time_difference.total_seconds() % 60:,.2f} seconds.')
        cropped = [ file for file in os.listdir(os.getcwd()) if file.startswith('Cropped_')]
        print()
        print(f'Total number of cropped files: {len(cropped)}')
        print('---------------------------')
        script_number +=1
    subprocess.Popen("rm Cropped_*.png")
    print('The test is finshed')
    return stdout, stderr


if __name__ == '__main__':
    test_start(valid_commands)
