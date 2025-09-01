
import os,sys,webbrowser

try:
	import tkinter as tk
	from tkinter import filedialog,messagebox
except ModuleNotFoundError as e:
	print("这个程序需要 tkinter 才能运行。")
	if input("安装 tkinter 吗？(输入Y(是)或其他(否))").upper == "Y":
		if sys.platform.startswith("darwin"):
			webbrowser.open("https://www.python.org/download/mac/tcltk/")
		elif sys.platform.startswith("linux"):
			os.system("sudo apt-get install python3-tk")
	exit()

if sys.version_info.major < 3:
	if messagebox.askyesno("文件加密","这个程序需要 Python 3.9 及以上的版本才能运行。前往安装界面吗？"):
		webbrowser.open("https://www.python.org/downloads/")
	exit()

if sys.version_info.minor < 9:
	if messagebox.askyesno("文件加密","这个程序需要 Python 3.9 及以上的版本才能运行。前往安装界面吗？"):
		webbrowser.open("https://www.python.org/downloads/")
	exit()

if os.system("openssl version") != 0:
	if messagebox.askyesno("文件加密","这个程序需要电脑上安装 OpenSSL 才能运行。前往安装界面吗？"):
		if sys.platform.startswith("win32"):
			webbrowser.open("https://slproweb.com/products/Win32OpenSSL.html")
		elif sys.platform.startswith("darwin"):
			os.system("brew install openssl")
			os.system("brew update openssl")
			




def encrypt():
	

	
	def onefile():
		def ok():
			if passwdentry.get() == repasswdentry.get():
				messagebox.showwarning("文件加密","1.接下来可能会弹出一个黑色终端窗口，请勿直接关闭，否则加密将失败！\n2.在加/解密较大文件时，当前程序可能会无响应1分钟左右。请耐心等待，谢谢！")
				returnvalue = os.system("openssl enc -aes-256-cbc -salt -in " + filename + " -out " + filename + ".after_encrypt -k "+passwdentry.get()) # Encrypt Command
				if returnvalue != 0:
					messagebox.showwarning("文件加密","加密失败。")
				else:
					messagebox.showinfo("文件加密","已加密文件\"" + filename + "\"。")
					nonlocal win01
					win01.destroy()
					del win01
					if messagebox.askyesno("文件加密","删除源文件吗？"):
						try:
							os.remove(filename)
						except Exception as e:
							messagebox.showerror("文件加密","出现问题：\n" + str(e))
						else:
							messagebox.showinfo("文件加密","成功删除源文件。")
			else:
				messagebox.showwarning("文件加密","两次输入的密码不同！")
		nonlocal stw
		stw.destroy()
		filename = filedialog.askopenfilename(filetypes=[("所有文件","*")])
		if filename != "":
			
			win01 = tk.Toplevel(rw)
			win01.resizable(0,0)
			win01.geometry("300x150")
			label1 = tk.Label(win01,text="请输入密码")
			label1.pack()
			passwdentry = tk.Entry(win01,show="*")
			passwdentry.pack()
			label2 = tk.Label(win01,text="请再次输入密码")
			label2.pack()
			repasswdentry = tk.Entry(win01,show="*")
			repasswdentry.pack()
			okbutton = tk.Button(win01,text="下一步",command=ok)
			okbutton.pack()
		else:
			messagebox.showwarning("文件加密","您未选择文件。")
	
	def onefolder():
		messagebox.showinfo("文件加密","即将上线！")
	stw = tk.Toplevel(rw)# Select Type Window 选择类型（单个文件/单文件夹）
	stw.geometry("100x100")
	b1 = tk.Button(stw,text="单个文件",command=onefile)
	b2 = tk.Button(stw,text="单个文件夹",command=onefolder)
	b1.pack()
	b2.pack()

# os.system("openssl enc -d -aes-256-cbc -in " + filename + " -out " + filename.removesuffix(".after_encrypt") + " -k " + label1.get()) # Encrypt Command
def deciphering():
	
	def onefile():
		def ok():
			messagebox.showwarning("文件加密","1.接下来可能会弹出一个黑色终端窗口，请勿直接关闭，否则解密将失败！\n2.在加/解密较大文件时，当前程序可能会无响应1分钟左右。请耐心等待，谢谢！")
			returnvalue = os.system("openssl enc -d -aes-256-cbc -in " + filename + " -out " + filename.removesuffix(".after_encrypt") + " -k " + passwdentry.get()) # Encrypt Command
			if returnvalue == 0:
				messagebox.showinfo("文件加密","已解密文件\"" + filename + "\"。")
				nonlocal win01
				win01.destroy()
				del win01
			else:
				messagebox.showwarning("文件加密","解密失败；可能是您输入的密码有误，请重新输入。")
				os.remove(filename.removesuffix(".after_encrypt"))
		nonlocal stw
		stw.destroy()

		filename = filedialog.askopenfilename(filetypes=[("加密后的文件","after_encrypt")])
		if filename != "":
			
			win01 = tk.Toplevel(rw)
			win01.resizable(0,0)
			win01.geometry("300x100")
			label1 = tk.Label(win01,text="请输入密码")
			label1.pack()
			passwdentry = tk.Entry(win01,show="*")
			passwdentry.pack()
			okbutton = tk.Button(win01,text="下一步",command=ok)
			okbutton.pack()
		else:
			messagebox.showwarning("文件加密","您未选择文件。")
	
	def onefolder():
		messagebox.showinfo("文件加密","即将上线！")
	
	
	stw = tk.Toplevel(rw)# Select Type Window 选择类型（单个文件/单文件夹）
	stw.geometry("100x100")
	b1 = tk.Button(stw,text="单个文件",command=onefile)
	b2 = tk.Button(stw,text="单个文件夹",command=onefolder)
	b1.pack()
	b2.pack()


rw = tk.Tk()
rw.resizable(0,0)
rw.geometry("180x100")

but1 = tk.Button(text="加密",command=encrypt)
but2 = tk.Button(text="解密",command=deciphering)

but1.pack()
but2.pack()

rw.mainloop()

