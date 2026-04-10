import subprocess


valid_commands = [
    'py main.py',                                                       # default script, i.e. processing wizards only
    'py main.py -v',                                                    # processing views
    'py main.py -w',                                                    # processing wizards
    'py main.py -x 100',                                                # processing views with the width value of 100
    'py main.py -y 100',                                                # processing views with the height value of 100
    'py main.py -x 100 -y 100',                                         # processing views with the width and height values of 100
    'py main.py -y 200 -x 200',                                         # processing views with the height and width values of 100
    'py main.py -f D:/py/viewCropper/Screenshot_1.png'                  # processing a wizard
    'py main.py -x 100 -f D:/py/viewCropper/Screenshot_2.png',          # processing a view with an X-coordinate first
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -x 100',          # processing a view with an X-coordinate last
    'py main.py -y 100 -f D:/py/viewCropper/Screenshot_2.png',          # processing a view with a Y-coordinate first
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -y 100',          # processing a view with a Y-coordinate last
    'py main.py -x 200 -y 200 -f D:/py/viewCropper/Screenshot_2.png',   # processing a view with an X-coordinate and a Y-coordinate first
    'py main.py -x 200 -f D:/py/viewCropper/Screenshot_2.png -y 200',   # processing a view with an X-coordinate first and a Y-coordinate last
    'py main.py -y 200 -f D:/py/viewCropper/Screenshot_2.png -x 200',   # processing a view with a Y-coordinate first and an X-coordinate last
    'py main.py -y 200 -x 200 -f D:/py/viewCropper/Screenshot_2.png',   # processing a view with a Y-coordinate and an X-coordinate first
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -x 200 -y 200',   # processing a view with an X-coordinate and a Y-coordinate last where X is before Y
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -y 200 -x 200',   # processing a view with an X-coordinate and a Y-coordinate last where Y is before 
    'py main.py -d -w',                                                 # processing wizards in the current folder
    'py main.py -d -v',                                                 # processing views in the current folder
    'py main.py -d -v -c',                                              # processing views in the current folder starting with Cropped_
    'py main.py -d -w -c'                                               # processing wizards in the current folder starting with Cropped_
]


invalid_commands = [
    'py main.py -x 100 -a 100',
    'py main.py -y 100 -a 100',
    'py main.py -a 100 -b 100',
    'py main.py -a -b',
    'py main.py -a'
]


def test_start(commands: list) -> tuple:
    script_number = 0
    print()
    from datetime import datetime
    for script in commands:
        print(f'starting the test: { script } ')
        start_time = datetime.now()
        process = subprocess.Popen(
            script,
            stdin   = subprocess.PIPE,
            stdout  = subprocess.PIPE,
            stderr  = subprocess.PIPE,
            text    = True
            )
        stdout, stderr = process.communicate(input='\n')
        end_time = datetime.now()
        time_difference = end_time - start_time
        print(f'"{ commands[script_number] }" finished at { time_difference.total_seconds() % 60 }')
        script_number +=1
    print('the test is finshed')
    return stdout, stderr


if __name__ == '__main__':
    test_start(valid_commands)
