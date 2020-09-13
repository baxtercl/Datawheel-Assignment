import os
import pathlib
from fnmatch import fnmatch
import csv

root = pathlib.Path().absolute()
pattern = '*_p*.csv'
filecsv = 'data.csv'

with open(filecsv, 'w', newline='') as csvfile:
	dw = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	dw.writerow(['State', 'Salary'])

total = 0
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
        	if (total >= 0):
        		filedata = os.path.join(path, name)
        		with open(filedata, 'r', newline='') as csvfilereader:
        			dr = csv.DictReader(csvfilereader)
        			for row in dr:
        				with open(filecsv, 'a', newline='') as csvfile:
        					datawriter = csv.writer(csvfile)
        					datawriter.writerow([row['ST'],row['WAGP']])
        		print(filedata)
        	total +=1
print(total)