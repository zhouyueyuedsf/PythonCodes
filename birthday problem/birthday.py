import random
import numpy as np  
import matplotlib.pyplot as plt

def initBirthday(n):
	birthdayRecord = []
	for i in range(n):
		birthdayRecord.append(random.randint(0, 364))
	return birthdayRecord

def checkDuplicate(a, b):
	if a == b:
		return True
	else:
		return False 

def simulatingBirth(n):
	birthRecordSample = []
	for i in range(1000):
		birthRecordSample.append(initBirthday(n))
	sameBirthCount = 0
	for i in range(1000):
		if len(birthRecordSample[i]) != len(set(birthRecordSample[i])):
			sameBirthCount = sameBirthCount + 1
	return sameBirthCount / 1000.0

def result():
	prob_n = []
	for i in range(2, 101):
		prob_n.append(simulatingBirth(i))
	return prob_n

def showPic(prob_n): 
	x = []  
	for i in range(2, 101):
		x.append(i)
	plt.plot(x, prob_n)
	plt.xlabel("n")
	plt.ylabel("probability")
	plt.title('probability vs n')
	plt.show()
	
def findPerc50(prob_n):
	for i in prob_n:
		if i >= 0.5:
			return prob_n.index(i) + 2


resultArr = result()
prob_n = np.array(resultArr)
print(prob_n)
perc_50 = findPerc50(resultArr)
print(perc_50)
showPic(resultArr)




