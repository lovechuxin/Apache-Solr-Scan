import tkinter as tk
from  tkinter  import ttk
from tkinter import scrolledtext, messagebox
from tkinter import *
import importlib
import os
import sys
import threading
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
window = tk.Tk()
window.title('solr漏洞检测工具 v1.1     by：chuxin')#窗口标题
window.geometry("805x511+286+71")#长高
# window.iconbitmap('123.ico')

def imp(ip,cmd,down):
    if ip:
        if down == 'all':
            from module.CVE_2017_12629 import main as qq
            from module.CVE_2019_0193 import main as ww
            from module.CVE_2019_17558 import main as ee
            from module.CVE_2020_13957 import main as rr
            from module.xxe_CVE_2017_12629 import main as tt
            from module.xxe_CVE_2018_1308 import main as yy
            from module.arbitrary_file_read import main as uu

            try:
                t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                t.see(tk.END);
                t.insert('end', ww(ip),tk.INSERT, '\n\n\n')
                t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);


            try:
                t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                t.see(tk.END);
                t.insert('end', ee(ip),tk.INSERT, '\n\n\n')
                t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

            try:
                t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                t.see(tk.END);
                t.insert('end', rr(ip),tk.INSERT, '\n\n\n')
                t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

            try:
                t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                t.see(tk.END);
                t.insert('end', tt(ip),tk.INSERT, '\n\n\n')
                t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

            try:
                t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                t.see(tk.END);
                t.insert('end', yy(ip),tk.INSERT, '\n\n\n')
                t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

            try:
                t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                t.see(tk.END);
                t.insert('end', qq(ip),tk.INSERT, '\n\n\n')
                t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

            try:
                t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                t.see(tk.END);
                t.insert('end', uu(ip),tk.INSERT, '\n\n\n')
                t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

            t.insert('end',"检测完成！",tk.INSERT, '\n\n')
            t.see(tk.END);

        elif down == "CVE-2017-12629":
            try:
                if cmd:
                    from module.CVE_2017_12629 import main1
                    t.insert('end', main1(ip,cmd),tk.INSERT, '\n\n\n')
                    t.see(tk.END);

                else:
                    from module.CVE_2017_12629 import main
                    t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                    t.insert('end', main(ip),tk.INSERT, '\n\n\n')
                    t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);


        elif down == "CVE-2019-0193":
            try:
                if cmd:
                    from module.CVE_2019_0193 import main1
                    t.insert('end', main1(ip,cmd),tk.INSERT, '\n\n\n')
                    t.see(tk.END);

                else:
                    from module.CVE_2019_0193 import main
                    t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                    t.insert('end', main(ip),tk.INSERT, '\n\n\n')
                    t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

        elif down == "CVE-2019-17558":
            try:
                if cmd:
                    from module.CVE_2019_17558 import main1
                    t.insert('end', main1(ip,cmd),tk.INSERT, '\n\n\n')
                    t.see(tk.END);

                else:
                    from module.CVE_2019_17558 import main
                    t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                    t.insert('end', main(ip),tk.INSERT, '\n\n\n')
                    t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

        elif down == "CVE-2020-13957":
            try:
                if cmd:
                    from module.CVE_2020_13957 import main1
                    t.insert('end', main1(ip,cmd),tk.INSERT, '\n\n\n')
                    t.see(tk.END);

                else:
                    from module.CVE_2020_13957 import main
                    t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                    t.insert('end', main(ip),tk.INSERT, '\n\n\n')
                    t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

        elif down == "arbitrary_file_read":
            try:
                if cmd:
                    from module.arbitrary_file_read import main1
                    t.insert('end',"正在读取请稍等···",tk.INSERT, '\n')
                    t.insert('end', main1(ip,cmd),tk.INSERT, '\n\n\n')
                    t.see(tk.END);

                else:
                    from module.arbitrary_file_read import main
                    t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                    t.insert('end', main(ip),tk.INSERT, '\n\n\n')
                    t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);


        elif down == "xxe_CVE-2017-12629":
            try:
                if cmd: 
                    t.insert('end', '目前不提供exp，请自行利用',tk.INSERT, '\n\n') #输出换行
                    t.see(tk.END);
                else:
                    from module.xxe_CVE_2017_12629 import main
                    t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                    t.insert('end', main(ip),tk.INSERT, '\n\n\n')
                    t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);

        elif down == "xxe_CVE-2018-1308":
            try:
                if cmd: 
                    t.insert('end', '目前不提供exp，请自行利用',tk.INSERT, '\n\n') #输出换行
                    t.see(tk.END);
                else:
                    from module.xxe_CVE_2018_1308 import main
                    t.insert('end',"正在检测请稍等···",tk.INSERT, '\n')
                    t.insert('end', main(ip),tk.INSERT, '\n\n\n')
                    t.see(tk.END);
            except:
                t.insert('end',"目标目标计算机积极拒绝，无法连接，请重试",tk.INSERT, '\n\n\n')
                t.see(tk.END);




def thread_it():
    '''将函数打包进线程'''
    # 创建
    var = e.get()
    var1 = e1.get()
    var2 = c.get()
    t = threading.Thread(target=imp,args=[var,var1,var2]) 
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


e = tk.Entry(window) #Entry 输入框
e.place(relx=0.062, rely=0.098, relheight=0.041, relwidth=0.591)

e1 = tk.Entry(window) #Entry 输入框
e1.place(relx=0.062, rely=0.176, relheight=0.041, relwidth=0.260)

l = tk.Label(window, text='''输入url       http://127.0.0.1:8983''',font=('Arial',10), width=25,height=2) #显示口
l.place(relx=0.075, rely=0.039, height=19, width=200)

l1 = tk.Label(window, text='''url：''',font=('Arial',9)) #显示口
l1.place(relx=0.025, rely=0.098, height=19, width=23)

l2 = tk.Label(window, text='''cmd：''',font=('Arial',9)) #显示口
l2.place(relx=0.012, rely=0.176, height=19, width=33)

b = tk.Button(window, text='漏洞验证', command=thread_it) #点击按钮
b.place(relx=0.86, rely=0.098, height=25, width=86)

t = scrolledtext.ScrolledText(window)#Entry 下拉的显示框
t.place(relx=0.012, rely=0.254, relheight=0.726, relwidth=0.976)


var = tk.StringVar()
c = ttk.Combobox(window, textvariable=var) #下拉框
c.place(relx=0.671, rely=0.098, relheight=0.041, relwidth=0.180)
c["values"]=("all","CVE-2017-12629","CVE-2019-0193","CVE-2019-17558","CVE-2020-13957","arbitrary_file_read","xxe_CVE-2017-12629","xxe_CVE-2018-1308")
c.current(0)  #选择第一个值  


window.mainloop()