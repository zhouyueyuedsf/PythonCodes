# -*- coding: utf-8 -*-
import os 
import pexpect
import shutil

root = '/Users/XFade/Desktop/shiyanerzuoye'
savepath = '/Users/XFade/Desktop/forpigaizuoye/'

def readCppFiles():
	cppFiles = []
	for rt, dirs, files in os.walk(root):
		for f in files:
			if f[-3:] == 'cpp' or f[-3:] == 'CPP':
				print(os.path.join(rt,f))
				cppFiles.append(os.path.join(rt,f))
				newfilename = os.path.join(rt,f)[os.path.join(rt,f).rfind('/')+1:]
				shutil.copyfile(os.path.join(rt,f), savepath + newfilename)
	return cppFiles

def judgeResult(filename):

	testStr = 'abFG45-=,'
	expectStr = 'ABfg45###'

	print('-----------------Begin------------------')
	print('It is the homework of ' + filename)

	sourcefilename = filename[filename.rfind('/')+1:]
	ofilename = filename[filename.rfind('/')+1:-4]

	os.system('g++ ' + savepath + sourcefilename + ' -o ' + savepath + ofilename)
	child = pexpect.spawn(savepath + ofilename)
	child.expect('')
	child.sendline(testStr)
	fout = open('mylog.txt','wb')
	child.logfile = fout
	child.interact()
	print('\n')

	lineList = []
	with open('mylog.txt','r') as f:
		for line in f.readlines():
			lineList.append(line.strip())

	outputStr = lineList[len(lineList)-1][:9] 
	with open('result.txt','a') as f:
		if outputStr == expectStr:
			f.write(filename + '\tCorrect!\n')
		else:
			f.write(filename + '\tError!\n')
	f.close()
	print('-----------------End------------------\n')

def main():
	cppFiles = readCppFiles()
	print(len(cppFiles))
	for filename in cppFiles:
		judgeResult(filename)

if __name__ == '__main__':
	main()