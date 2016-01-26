# ann.py

import sys

def readFileToDataPoint(filename):
	with open(filename, 'r') as f:
		for line in f:
			print(line)


if len(sys.argv) is 2:
	readFileToDataPoint(sys.argv[1])
else:
	print("no arg")