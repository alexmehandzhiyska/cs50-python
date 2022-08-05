import sys
import os.path
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

file_name = sys.argv[1]

if not file_name.endswith('.csv'):
    sys.exit('Not a CSV file')

if not os.path.isfile(file_name):
    sys.exit('File does not exist')

headers = []
pizzas = []

with open(file_name, 'r') as file:
    csv_reader = list(csv.reader(file, delimiter = ','))
    
    headers = csv_reader[0]
    
    for col in csv_reader[1:]:
        pizzas.append(col)

table = tabulate(pizzas, headers, tablefmt='grid')
print(table)