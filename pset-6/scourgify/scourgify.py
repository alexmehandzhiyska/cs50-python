import sys
import os.path
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

original_file_name = sys.argv[1]
new_file_name = sys.argv[2]

if not original_file_name.endswith('.csv'):
    sys.exit('Not a CSV file')

if not os.path.isfile(original_file_name):
    sys.exit('File does not exist')

with open(original_file_name, 'r') as original_file:
    csv_reader = list(csv.reader(original_file))

    with open(new_file_name, 'w') as new_file:
        wr = csv.writer(new_file)
        wr.writerow(['first', 'last', 'house'])

        for line in csv_reader[1:]:
            name, house = line
            last, first = name.split(', ')

            wr.writerow([first, last, house])