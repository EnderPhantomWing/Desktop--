import tkinter as tk
from tkinter import StringVar
import webbrowser
import time

def open_url():
    webbrowser.open('https://www.bilibili.com/video/BV1GJ411x7h7') 
def open_url2():
    webbrowser.open('https://www.bilibili.com/')
def open_url3():
    webbrowser.open('https://zh.minecraft.wiki')
def open_url4():
    webbrowser.open('https://minecraft.net')
def open_url5():
    webbrowser.open('https://space.bilibili.com/3493136428960296')
    
def check_input():
    if entry.get().isdigit:
        button.config(state=tk.NORMAL)
    else:
        button.config(state=tk.DISABLED)
        
def button_click():
    btn1.config(state=tk.NORMAL)
    btn2.config(state=tk.NORMAL)
    btn7.config(state=tk.NORMAL)
    btn8.config(state=tk.NORMAL)
    label3.config(text="请尽情使用吧！")


root = tk.Tk()
root.title('Desktop--')
root.geometry('749x450')


#按键区
btn1= tk.Button(root,width=20, text='点我有惊喜',activeforeground='blue',command=open_url, state=tk.DISABLED)
btn1.grid(column=0, row=4)
btn2= tk.Button(root,width=20, text='Bilibili,启动！',activeforeground='blue', command=open_url2,state=tk.DISABLED)
btn2.grid(column=1, row=4)
btn7=tk.Button(root,width=20,text='MC Wiki 大中华区',activeforeground='blue',command=open_url3,state=tk.DISABLED)
btn7.grid(column=2,row=4)
btn8=tk.Button(root,width=20,text='Minecraft官网',activeforeground='blue',command=open_url4,state=tk.DISABLED)
btn8.grid(column=3,row=4)
btn9=tk.Button(root,width=20,text='作者のB站',activeforeground='blue',command=open_url5,state=tk.NORMAL)
btn9.grid(column=4,row=4)
button = tk.Button(root, text="Log in",activeforeground='red',command=button_click,state=tk.DISABLED)
button.grid(column=3,row=3)

#字
label2=tk.Label(root,text="Password(随便输一个数):")
label2.grid(row=0,column=2)
label3=tk.Label(root,text="")
label3.grid(row=0,column=4)

#输入区
entry=tk.Entry(root,show="*")
entry.grid(row=0, column=3)

entry.bind("<KeyRelease>", lambda event: check_input())


# 获取时间的函数
def gettime():
    # 获取当前时间
    dstr.set(time.strftime("%H:%M:%S"))
    # 每隔 1s 调用一次 gettime()函数来获取时间
    root.after(1000, gettime)
    root.update()
def gettime2():
    # 获取当前时间
    dstr2.set(time.strftime("%D"))
    # 每隔 1s 调用一次 gettime()函数来获取时间
    root.after(1000, gettime2)
    root.update()
# 生成动态字符串
dstr = StringVar()
dstr2 = StringVar()
# 利用 textvariable 来实现文本变化
label4 = tk.Label(root, textvariable=dstr, fg='black', font=("微软雅黑", 20))
label4.grid(row=0,column=1)
label5 = tk.Label(root, textvariable=dstr2, fg='black', font=("微软雅黑", 20))
label5.grid(row=0,column=0)
# 调用生成时间的函数
gettime()
gettime2()
# 显示窗口


root.mainloop()
