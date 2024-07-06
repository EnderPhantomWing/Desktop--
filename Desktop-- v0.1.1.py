import tkinter as tk
from tkinter import StringVar
import tkinter.messagebox
import webbrowser
import time

root = tk.Tk()
root.title('Desktop-- v1.1')
root.geometry('749x450')


#功能区
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
def open_url6():
    webbrowser.open('https://www.bilibili.com/video/BV1TAhGeEEzp')
def open_url7():
    webbrowser.open('https://space.bilibili.com/1546229901')
def open_url8():
    webbrowser.open('https://www.mcmod.cn')
def open_url9():
    webbrowser.open('https://modrinth.com')
def open_url10():
    webbrowser.open('https://www.curseforge.com')
def open_url11():
    webbrowser.open('https://mc.163.com')
def open_url12():
    webbrowser.open('https://space.bilibili.com/697635368')

def check_input():
    if entry.get().isdigit and int(entry.get()) == 114514:
        button.config(state=tk.NORMAL)
    else:
        button.config(state=tk.DISABLED)

def do_job():
    tkinter.messagebox.showerror(title='Sorry',message='还未开发完成，请敬请期待')
menubar=tk.Menu(root)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New', command=do_job,accelerator='Ctrl+N')
filemenu.add_command(label='Open', command=do_job,accelerator='Ctrl+O')
filemenu.add_command(label='Save', command=do_job,accelerator='Ctrl+S')
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=root.quit,accelerator='Ctrl+Q')
submenu = tk.Menu(filemenu,tearoff=0) # 和上面定义菜单一样，不过此处实在File上创建一个空的菜单
submenu2 = tk.Menu(filemenu,tearoff=0)
submenu.add_command(label='关于作者EnderPhantomWing', command=open_url5)
submenu.add_command(label='关于茶水晶服务器腐竹Redapple_one',command=open_url7)
filemenu.add_cascade(label='茶水晶服务器，欢迎加群游玩！',menu=submenu2,underline=0)
submenu2.add_command(label='审核群群号：733583058')
filemenu.add_cascade(label='About', menu=submenu, underline=0)# 给放入的菜单submenu命名为Import
filemenu.add_command(label='别看了，分隔线上边的都是摆设')


def button_click():
    btn1.config(state=tk.NORMAL)
    btn2.config(state=tk.NORMAL)
    btn3.config(state=tk.NORMAL)
    btn4.config(state=tk.NORMAL)
    btn5.config(state=tk.NORMAL)
    btn6.config(state=tk.NORMAL)
    btn7.config(state=tk.NORMAL)
    btn8.config(state=tk.NORMAL)
    btn10.config(state=tk.NORMAL)
    tkinter.messagebox.showinfo(title='Tips',message='请尽情使用吧！')


#按键区
btn1= tk.Button(root,width=20, text='点我有惊喜',activeforeground='blue',command=open_url, state=tk.DISABLED)
btn1.grid(column=0, row=4)
btn2= tk.Button(root,width=20, text='Bilibili,启动！',activeforeground='blue', command=open_url2,state=tk.DISABLED)
btn2.grid(column=1, row=4)
btn3= tk.Button(root,width=20, text='MC Mod',activeforeground='blue', command=open_url8,state=tk.DISABLED)
btn3.grid(column=0, row=5)
btn4= tk.Button(root,width=20, text='Modrinth',activeforeground='blue', command=open_url9,state=tk.DISABLED)
btn4.grid(column=1, row=5)
btn5= tk.Button(root,width=20, text='CurseForge',activeforeground='blue', command=open_url10,state=tk.DISABLED)
btn5.grid(column=2, row=5)
btn6= tk.Button(root,width=20, text='MC中国版（冈易）',activeforeground='blue', command=open_url11,state=tk.DISABLED)
btn6.grid(column=3, row=5)
btn7=tk.Button(root,width=20,text='MC Wiki 大中华区',activeforeground='blue',command=open_url3,state=tk.DISABLED)
btn7.grid(column=2,row=4)
btn8=tk.Button(root,width=20,text='Minecraft官网',activeforeground='blue',command=open_url4,state=tk.DISABLED)
btn8.grid(column=3,row=4)
btn9=tk.Button(root,width=20,text='作者の最新作品',activeforeground='blue',command=open_url6,state=tk.NORMAL)
btn9.grid(column=4,row=4)
btn10=tk.Button(root,width=20,text='呱兄B站个人主页',activeforeground='blue',command=open_url12,state=tk.DISABLED)
btn10.grid(column=4,row=5)
button = tk.Button(root, text="Log in",activeforeground='red',command=button_click,state=tk.DISABLED)
button.grid(column=3,row=3)

#字
label2=tk.Label(root,text="Password(默认114514):")
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

root.config(menu=menubar)

root.mainloop()
