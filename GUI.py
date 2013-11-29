#!/usr/bin/python
#encoding:utf-8

from Tkinter import *


class ToolGUI:
	def __init__(self):
		self.root = root= Tk();
		root.title("ChangWord V1.0")
		#self.screen_width = screen_width = root.winfo_screenwidth()
        #self.screen_height = screen_height = root.winfo_screenheight() - 100
		root.geometry('600x300')
		
		self.lable = Label(root, text=u'工程地址:')
		self.lable.grid(row=1, column=0, padx=5, pady=10)
		self.proLocation = Entry(width=30)		
		self.proLocation.grid(row=1, column=1, sticky=W, padx=10, pady=10)
		self.browse = Button(root, text=u'浏览', width=5, justify=RIGHT, command=lambda: self.locateProject(self))
		self.browse.grid(row=1, column=2, sticky=E, padx=5, pady=10)
		
		self.label = Label(root, text = u'词条ID或名称： ')
		self.label.grid(row=2, column=0, padx=5, pady=10)
		self.id = Entry(width=20)
		self.id.grid(row=2, column=1, padx=5, sticky=E, pady=10)
		self.lang = StringVar(root)
		self.lang.set("CN") # default value
		self.langOption = OptionMenu(root, self.lang, "IN", "RU", "TH")
		self.langOption.grid(row=2, column=2, padx=5, pady=10)
		print  self.lang
		
		scrollbar = Scrollbar(root)
		#scrollbar.pack(side=RIGHT, fill=Y)

		listbox = Listbox(root, yscrollcommand=scrollbar.set)
		for i in range(1000):
			listbox.insert(END, str(i))
		#listbox.pack(side=LEFT, fill=BOTH)

		#scrollbar.config(command=listbox.yview)

	def locateProject(self):
		pass