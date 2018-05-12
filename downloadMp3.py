#encoding:utf-8

import os
import urllib
from Tkinter import *
from bs4 import BeautifulSoup

serverUrl = ''
voiceUrl = 'http://res.wx.qq.com/voice/getvoice?mediaid='
localUrl = '/Users/XFade/Desktop/'

def getHtml(url):  
    html = urllib.urlopen(url).read()  
    return html 

def saveHtml(file_name, file_content):  
    with open(file_name + ".html", "wb") as f:  
        # 写文件用bytes而不是str，所以要转码  
        f.write(file_content)  

def schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)

def downloadMP3():
	serverUrl = inputAddress.get()
	saveHtml(localUrl + serverUrl[26:], getHtml(serverUrl))
	soup = BeautifulSoup(open(localUrl + serverUrl[26:] + ".html"), "html.parser")
	voiceIds = []
	for voice in soup.find_all('mpvoice'):
		voiceIds.append(voice.get('voice_encode_fileid'))
	for voiceId in voiceIds:
		local = os.path.join(localUrl, voiceId + '.mp3')
		urllib.urlretrieve(voiceUrl + voiceId, local)

top = Tk()   #主窗口
top.geometry('600x400')  #设置了主窗口的初始大小600x400
label = Label(top,text='下载微信公众号音乐', font='Helvetica -20 bold')  #设置标签字体的初始大小
label.pack(fill = Y, expand=1)
inputAddress = Entry(top, text="请输入网址")
inputAddress.pack(fill = X, expand=1)
downloadBtn = Button(top, text='Download', command=downloadMP3)
downloadBtn.pack()
mainloop()


        

