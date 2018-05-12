# -*- coding: utf-8 -*-

import shutil
savepath = '/Users/XFade/Desktop/forpigaizuoye/'
filename = "/Users/XFade/Desktop/shiyanerzuoye/陈一玮,(20161800)/提交作业的附件/20161800陈一玮2.cpp"
newfilename = filename[filename.rfind('/')+1:]
ofilename = filename[filename.rfind('/')+1:-4]
print(ofilename)

shutil.copyfile(filename, savepath+newfilename)
