import sys #for argv
import string #for index
import re #for sub
import csv

from math import *

def isInt(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

def isFloat(x):
	try:
		float(x)
		return True
	except ValueError:
		return False

def repl(match):
	token = match.group(0)
	letter = token[0] #only one letter in token!
	index1 = string.ascii_uppercase.index(letter)
	index2 = int(token[1:]) - 1
	res = "data[" + str(index2) + "][" + str(index1) + "]"
	return res

g = {}
l = {}
#getting args
if len(sys.argv) > 2:
	inFile = sys.argv[1]
	outFile = sys.argv[2]
	script = None
if len(sys.argv) == 4:
	script = sys.argv[3]
	sF = open(script)
	scr = sF.read()
	sF.close()
	exec(scr, g, l)

#reading input
data = []
inFile = open(inFile, newline='')
reader = csv.reader(inFile, delimiter = ',', quotechar = '"')
for row in reader:
	data.append(row)
inFile.close()

#preparing result
for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j][0] == '=':
			code = re.sub('[A-Z][0-9]*', repl, data[i][j][1:])
			try:
				res = eval(code, globals(), l)
				data[i][j] = res
			except:
				data[i][j] = "ERROR"
		else:
			if isFloat(data[i][j]):
				if isInt(data[i][j]) and int(data[i][j]) == float(data[i][j]):
					data[i][j] = int(data[i][j])
				else:
					data[i][j] = float(data[i][j])
				

#print the result
oCSV = open(outFile, 'w', newline = '')
writer = csv.writer(oCSV, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
for x in data:
	writer.writerow(x)
oCSV.close()