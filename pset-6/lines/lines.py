import sys
import os.path

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

file_name = sys.argv[1]

if not file_name.endswith('.py'):
    sys.exit('Not a Python file')

if not os.path.isfile(file_name):
    sys.exit('File does not exist')

loc = 0

with open (file_name, 'r') as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()

        if not line.startswith('#') and not line == '':
            loc += 1

print(loc)