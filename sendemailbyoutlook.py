import win32com.client as win32 
from win32com import client as wc
import xlrd 
from tkinter import *
from tkinter import messagebox
#from tkinter.filedialog import askdirectory
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
	#print("get receivers succeed!")
	return result
	
def readContent(wordName):
	word = wc.Dispatch('Word.Application')
	doc = word.Documents.Open(wordName)
	doc.SaveAs(wordName.split(".")[0] + ".txt", 4)
	doc.Close()
	word.Quit()
	f = open(wordName.split(".")[0] + ".txt", 'r')
	#print("get email content succeed!")
	return f.read()

def sendEmail(subject, content, receiversNames, receivers, attachments):
	outlook = win32.Dispatch('outlook.application') 
	for i in range(len(receivers)):
		print("I am sending to " + receivers[i])
		mail = outlook.CreateItem(0)
		mail.To = receivers[i] 
		mail.Subject = subject
		Truecontent = "Dear, " + receiversNames[i] + content
		mail.Body = Truecontent
		for a in attachments:
			mail.Attachments.Add(a)
		mail.Send()
	print("Send succeed!")

class WidgetsDemo:
	def __init__(self):
		window = Tk()    
		window.title("Outlook群发邮件助手")
		frame2 = Frame(window)
		frame2.pack()

		self.excelName = StringVar()
		self.wordName = StringVar()
		self.attachments = StringVar()
		self.subject = StringVar()

		Label(frame2,text = "选择联系人Excel文件:").grid(row = 0, column = 0)
		Entry(frame2, width = 80, state='readonly', textvariable = self.excelName).grid(row = 0, column = 1)
		Button(frame2, text = "  . . .  ", command = self.selectExcelPath).grid(row = 0, column = 2)

		Label(frame2, text = "选择发送内容的Word文件:").grid(row = 1, column = 0)
		Entry(frame2, width = 80, state='readonly', textvariable = self.wordName).grid(row = 1, column = 1)
		Button(frame2, text = "  . . .  ", command = self.selectWordPath).grid(row = 1, column = 2)

		Label(frame2, text = "附件路径(可选):").grid(row = 2, column = 0)
		Entry(frame2, width = 80, state='readonly', textvariable = self.attachments).grid(row = 2, column = 1)
		Button(frame2, text = "  . . .  ", command = self.selectAttachments).grid(row = 2, column = 2)

		Label(frame2, text = "邮件主题").grid(row = 3, column = 0)
		Entry(frame2, width = 80, textvariable = self.subject).grid(row = 3, column = 1)

		btGetName = Button(frame2, width = 10, text = "发送", command = self.send)
		btGetName.grid(row = 4, column = 1)
		self.text = Text(window, state='normal')
		self.text.bind("<KeyPress>", lambda e: "break")
		self.text.pack()
		self.text.insert(INSERT, "使用说明：\n1.选择的excel文件需为xlsx格式的，里面包含两列内容，第一列为称呼，第二列\
为该收件人的邮箱地址，格式示例如下：\n名称\t\t邮箱\nAlice\txxxxxxxx@qq.com\nBob\txxxxxxxxx@163.com\n...\t\t......\n\n\
2.选择的word文件需要docx或doc格式的，里面包含发送的内容的模板；\n\n3.谢谢使用！\n")
		window.mainloop()

	def selectExcelPath(self):
		path_ = askopenfilename(filetypes = [("Excel File", "*.xlsx")])
		self.excelName.set(path_)

	def selectWordPath(self):
		path_ = askopenfilename(filetypes = [('docx file', '*.docx'), ('doc file', '*.doc')])
		self.wordName.set(path_)

	def selectAttachments(self):
		path_ = askopenfilenames()
		print(repr(path_))
		self.attachments.set(path_)

	def send(self):
		excelName = self.excelName.get()
		wordName = self.wordName.get()
		subject = self.subject.get()
		attachments = []
		if self.attachments.get() != "":
			filesNames = self.attachments.get()
			if filesNames.find("', '") == -1:
				attachments.append(filesNames[2:len(filesNames)-3])
			else:
				attachments = filesNames[2:len(filesNames)-2].split("', '")
		if excelName == "" or wordName == "":
			messagebox.showinfo('群发邮件', '请选择excel和word的文件路径！')
			return
		if subject == "":
			messagebox.showinfo('群发邮件', '请填写邮件主题！')
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
		sendEmail(subject, emailTemplate[7:], names, receivers, attachments)
		self.text.insert(INSERT, "发送成功！\n")
		self.text.update()
		messagebox.showinfo('群发邮件', '发送成功！')

WidgetsDemo()





