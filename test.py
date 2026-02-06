import subprocess
import datetime


valid_script_commands = [
    'py main.py',                                                       # default script, i.e. processing wizards only
    'py main.py -v',                                                    # processing views
    'py main.py -w',                                                    # processing wizards
    'py main.py -x 100',                                                # processing views with the width value of 100
    'py main.py -y 100',                                                # processing views with the height value of 100
    'py main.py -x 100 -y 100',                                         # processing views with the width and height values of 100
    'py main.py -y 200 -x 200',                                         # processing views with the height and width values of 100
    'py main.py -f D:/py/viewCropper/Screenshot_1.png'                  # processing a single file, i.e. a wizard
    'py main.py -x 100 -f D:/py/viewCropper/Screenshot_2.png',          # processing a single file, i.e. a view with an X-coordinate first  
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -x 100',          # processing a single file, i.e. a view with an X-coordinate last
    'py main.py -y 100 -f D:/py/viewCropper/Screenshot_2.png',          # processing a single file, i.e. a view with a Y-coordinate first
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -y 100',          # processing a single file, i.e. a view with a Y-coordinate last
    'py main.py -x 200 -y 200 -f D:/py/viewCropper/Screenshot_2.png',   # processing a single file, i.e. a view with an X-coordinate and a Y-coordinate first  
    'py main.py -x 200 -f D:/py/viewCropper/Screenshot_2.png -y 200',   # processing a single file, i.e. a view with an X-coordinate first and a Y-coordinate last  
    'py main.py -y 200 -f D:/py/viewCropper/Screenshot_2.png -x 200',   # processing a single file, i.e. a view with a Y-coordinate first and an X-coordinate last
    'py main.py -y 200 -x 200 -f D:/py/viewCropper/Screenshot_2.png',   # processing a single file, i.e. a view with a Y-coordinate and an X-coordinate first
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -x 200 -y 200',   # processing a single file, i.e. a view with an X-coordinate and a Y-coordinate last where X is before Y
    'py main.py -f D:/py/viewCropper/Screenshot_2.png -y 200 -x 200'    # processing a single file, i.e. a view with an X-coordinate and a Y-coordinate last where Y is before X
] 

not_valid_script_commands = [
    'py main.py -x 100 -a 100',
    'py main.py -y 100 -a 100',
    'py main.py -a 100 -b 100',
    'py main.py -a -b',
    'py main.py -a',
]


script_number = 0
print('starting the test...')
print() 
for script in valid_script_commands:
    process = subprocess.Popen(
        script, 
        stdin   = subprocess.PIPE, 
        stdout  = subprocess.PIPE, 
        stderr  = subprocess.PIPE, 
        text    = True
        )
    stdout, stderr = process.communicate(input='\n')          
    print(f'"{valid_script_commands[script_number]}" finished at {datetime.datetime.now().strftime("%H:%M:%S")}')            
    script_number +=1
print('the test is finshed')
