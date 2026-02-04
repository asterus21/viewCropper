import os, subprocess
import datetime

valid_script_commands = [
    'py main.py',
    'py main.py -v',
    'py main.py -w',
    'py main.py -x 100',
    'py main.py -y 100',
    'py main.py -x 100 -y 100',
    'py main.py -y 200 -x 200'
] 

not_valid_script_commands = [
    'py main.py -x 100 -a 100',
    'py main.py -y 100 -a 100',
    'py main.py -a 100 -b 100',
    'py main.py -a -b',
    'py main.py -a',
]


print(os.getcwd())
now = datetime.datetime.now()
for command in valid_script_commands:
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input='\n')
    print(f'finished at {now}')