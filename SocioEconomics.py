import csv

def Status(zip):
	with open('Economics.csv', 'rb') as f:
		reader = csv.reader(f)
		lis = list(reader)
	for e in lis:
		if str(zip) in str(e):
			return int(float(str(e[1]).replace(",", '')))