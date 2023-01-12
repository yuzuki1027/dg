import csv
import json
 

with open('urls.csv', 'r') as f:
    d_reader = csv.DictReader(f)
    d_list = [row for row in d_reader]
 

with open('output.json', 'w',encoding='utf-8') as f:
    json.dump(d_list, f)