import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import xlrd 
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames

def getReceivers(excelName):
	workbook = xlrd.open_workbook(excelName) 
	mySheet = workbook.sheet_by_index(0) 
	nrows = mySheet.nrows
	receivers = []
	names = []  
	for i in range(1, nrows): 
		receivers.append(mySheet.row_values(i)[1])
		names.append(mySheet.row_values(i)[0])
	result = []
	result.append(receivers)
	result.append(names)
	return result
	
def readContent(wordName):
	f = open(wordName.split(".")[0] + ".txt", 'r')
	return f.read()

def sendEmail(username, password, subject, content, receiversNames, receivers, attachments):
	server = smtplib.SMTP()
	server.connect('smtp.163.com')
	server.login(username, password)
	
	for i in range(len(receivers)):
		msg = MIMEMultipart()
		print("I am sending to " + receivers[i])
		msg['to'] = ','.join([receivers[i]])
		msg['from'] = username
		msg['subject'] = subject
		msg.attach(MIMEText("Dear, " + receiversNames[i] + content, 'plain', 'utf-8'))
		for a in attachments:
			att = MIMEText(open(a, 'rb').read(), 'base64', 'gb2312')
			att["Content-Type"] = 'application/octet-stream'
			att["Content-Disposition"] = 'attachment; filename=' + a.split('/')[len(a.split('/'))-1]
			msg.attach(att)	
		server.sendmail(msg['from'], msg['to'], msg.as_string())
	print("Send succeed!")

class WidgetsDemo:
	def __init__(self):
		window = Tk()    
		window.title("163邮箱群发邮件助手")
		frame2 = Frame(window)
		frame2.pack()

		self.excelName = StringVar()
		self.wordName = StringVar()
		self.attachments = StringVar()
		self.subject = StringVar()

		self.username = StringVar()
		self.password = StringVar()

		Label(frame2,text = "选择联系人Excel文件:").grid(row = 0, column = 0)
		Entry(frame2, width = 80, state='readonly', textvariable = self.excelName).grid(row = 0, column = 1)
		Button(frame2, text = "  . . .  ", command = self.selectExcelPath).grid(row = 0, column = 2)

		Label(frame2, text = "选择发送内容的Txt文件:").grid(row = 1, column = 0)
		Entry(frame2, width = 80, state='readonly', textvariable = self.wordName).grid(row = 1, column = 1)
		Button(frame2, text = "  . . .  ", command = self.selectWordPath).grid(row = 1, column = 2)

		Label(frame2, text = "附件路径(可选):").grid(row = 2, column = 0)
		Entry(frame2, width = 80, state='readonly', textvariable = self.attachments).grid(row = 2, column = 1)
		Button(frame2, text = "  . . .  ", command = self.selectAttachments).grid(row = 2, column = 2)

		Label(frame2,text = "用户名：").grid(row = 3, column = 0)
		Entry(frame2, width = 80, textvariable = self.username).grid(row = 3, column = 1)

		Label(frame2,text = "密码：").grid(row = 4, column = 0)
		Entry(frame2, width = 80, textvariable = self.password).grid(row = 4, column = 1)
		

		Label(frame2, text = "邮件主题").grid(row = 5, column = 0)
		Entry(frame2, width = 80, textvariable = self.subject).grid(row = 5, column = 1)

		btGetName = Button(frame2, width = 10, text = "发送", command = self.send)
		btGetName.grid(row = 6, column = 1)
		self.text = Text(window, state='normal')
		self.text.bind("<KeyPress>", lambda e: "break")
		self.text.pack()
		self.text.insert(INSERT, "使用说明：\n1.选择的excel文件需为xlsx格式的，里面包含两列内容，第一列为称呼，第二列\
为该收件人的邮箱地址，格式示例如下：\n名称\t\t邮箱\nAlice\txxxxxxxx@qq.com\nBob\txxxxxxxxx@163.com\n...\t\t......\n\n\
2.选择的word文件需要txt格式的，里面包含发送的内容的模板；\n\n3.谢谢使用！\n")
		window.mainloop()

	def selectExcelPath(self):
		path_ = askopenfilename(filetypes = [("Excel File", "*.xlsx")])
		self.excelName.set(path_)

	def selectWordPath(self):
		path_ = askopenfilename(filetypes = [('docx file', '*.txt')])
		self.wordName.set(path_)

	def selectAttachments(self):
		path_ = askopenfilenames()
		print(repr(path_))
		self.attachments.set(path_)

	def send(self):
		excelName = self.excelName.get()
		wordName = self.wordName.get()
		subject = self.subject.get()

		username = self.username.get()
		password = self.password.get()

		attachments = []
		if self.attachments.get() != "":
			filesNames = self.attachments.get()
			if filesNames.find("', '") == -1:
				attachments.append(filesNames[2:len(filesNames)-3])
			else:
				attachments = filesNames[2:len(filesNames)-2].split("', '")
		if excelName == "" or wordName == "":
			messagebox.showinfo('163邮箱群发邮件助手', '请选择excel和word的文件路径！')
			return
		if username == "" or password == "":
			messagebox.showinfo('163邮箱群发邮件助手', '请填写用户名和密码！')
			return
		if subject == "":
			messagebox.showinfo('163邮箱群发邮件助手', '请填写邮件主题！')
			return
		result = getReceivers(excelName)
		receivers = result[0]
		names = result[1]
		self.text.insert(INSERT, "获取联系人信息成功！\n")
		self.text.update()
		emailTemplate = readContent(wordName)
		self.text.insert(INSERT, "获取邮件内容成功！\n")
		self.text.update()
		self.text.insert(INSERT, "正在发送...\n")
		self.text.update()
		sendEmail(username, password, subject, emailTemplate[7:], names, receivers, attachments)
		self.text.insert(INSERT, "发送成功！\n")
		self.text.update()
		messagebox.showinfo('163邮箱群发邮件助手', '发送成功！')

WidgetsDemo()
