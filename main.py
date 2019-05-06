import os
import re
import datetime

filePath = "server-day.txt"

dictElement = {
	"Boot and services": "1",
	"Memory and Processes": "2",
	"Cryptography": "3",
	"Databases": "4",
	"Users, Groups and Authentication": "5"
}

def getPath():
	day = datetime.datetime.now()
	day = str(day.date()).replace("-","")
	files = os.popen('ls ' + day + '/ ').read()
	files = files.split("\n")
	print files
	
	for file in files:
		if file:
			getResult(day + "/" + file)
		else:
			print "Done!"
	
def getResult(filePath):
	text = "\n"
	f=open(filePath)
	lines=f.readlines()
	for i in range(1, len(lines)):
		if "Results" in lines[i]:
			for j in range(i, len(lines)):
				if "Suggestions" not in lines[j]:
					text = text + lines[j]
				else:
					break
	print text

def getElements():
	for key in dictElement.keys():
		line = os.popen('grep -n "' + key + '" ' + filePath).read()
		line = re.findall(r'\d+', line)
		dictElement[key] = int(line[0])

def getSubElements():
	text = "\n"
	f = open(filePath)
	lines = f.readlines()

	for key in dictElement.keys():
		num = dictElement[key] - 1
		if "-" in lines[num + 2]:
			while ("[+]" not in lines[num + 1]):
				text += lines[num].strip() + "\n"
				num += 1	

	print text

def getSuggestions():
	text = "\n"
	f=open(filePath)
	lines=f.readlines()
	for i in range(1, len(lines)):
		flag = len(lines)
		if "Suggestions" in lines[i]:
			text = text + lines[i]
			flag = i
			
			for j in range(i, len(lines)):
				if "*" in lines[j]:
					text = text + lines[j]
					j+=1
		

	print text

getPath()
#getResult()
# getElements()
# getSubElements()
# getSuggestions()
