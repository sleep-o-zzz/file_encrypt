
import os,sys

try:
	import tkinter as tk
	from tkinter import filedialog,messagebox
except ModuleNotFoundError as e:
	print("这个程序需要 tkinter 才能运行。")
	exit()

if sys.version_info.major < 3:
	messagebox.showerror("文件加密","这个程序需要 Python 3.9 及以上的版本才能运行。")
	exit()

if sys.version_info.minor < 9:
	messagebox.showerror("文件加密","这个程序需要 Python 3.9 及以上的版本才能运行。")
	exit()

if os.system("openssl version") != 0:
	messagebox.showerror("文件加密","这个程序需要电脑上安装 OpenSSL 才能运行。")




def encrypt():
	def ok():
		if passwdentry.get() == repasswdentry.get():
			os.system("openssl enc -aes-256-cbc -salt -in " + filename + " -out " + filename + ".after_encrypt -k "+passwdentry.get()) # Encrypt Command
			messagebox.showinfo("文件加密","已加密文件\"" + filename + "\"。")
			nonlocal win01
			win01.destroy()
			del win01
		else:
			messagebox.showwarning("文件加密","两次输入的密码不同！")

	filename = filedialog.askopenfilename(filetypes=[("所有文件","*")])
	if filename != "":
		
		win01 = tk.Toplevel(rw)
		win01.resizable(0,0)
		win01.geometry("300x200")
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

# os.system("openssl enc -d -aes-256-cbc -in " + filename + " -out " + filename.removesuffix(".after_encrypt") + " -k " + label1.get()) # Encrypt Command
def deciphering():
	def ok():
		returnvalue = os.system("openssl enc -d -aes-256-cbc -in " + filename + " -out " + filename.removesuffix(".after_encrypt") + " -k " + passwdentry.get()) # Encrypt Command
		if returnvalue == 0:
			messagebox.showinfo("文件加密","已解密文件\"" + filename + "\"。")
			nonlocal win01
			win01.destroy()
			del win01
		else:
			messagebox.showwarning("文件加密","您输入的密码有误，请重新输入。")

	filename = filedialog.askopenfilename(filetypes=[("加密后的文件","after_encrypt")])
	if filename != "":
		
		win01 = tk.Toplevel(rw)
		win01.resizable(0,0)
		win01.geometry("300x200")
		label1 = tk.Label(win01,text="请输入密码")
		label1.pack()
		passwdentry = tk.Entry(win01,show="*")
		passwdentry.pack()
		okbutton = tk.Button(win01,text="下一步",command=ok)
		okbutton.pack()
	else:
		messagebox.showwarning("文件加密","您未选择文件。")


rw = tk.Tk()
rw.resizable(0,0)
rw.geometry("300x200")

but1 = tk.Button(text="加密",command=encrypt)
but2 = tk.Button(text="解密",command=deciphering)

but1.pack()
but2.pack()

rw.mainloop()

