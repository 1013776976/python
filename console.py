import ctypes
import tkinter
import os
import webbrowser




#main
root = tkinter.Tk()
#watch clear
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#mian body
root.title("控制台")
#body location
root.geometry("+950+100")
root['bg'] = 'white'




#function
def a():
    os.system(r"start D:\object")
def b():
    os.system(r" taskkill /f /t /im msedge.exe")
def c():
    webbrowser.open('https://weibo.com/')


#button
button1 = tkinter.Button(root,text="临时文件",width=15,height=2,bg="moccasin",command=a)
button1.grid(row=0,column=1)
button2 = tkinter.Button(root,text="微博",width=15,height=2,bg="indianred",command=b)
button2.grid(row=0,column=2)
button3 = tkinter.Button(root,text="关闭浏览器",width=15,height=2,bg="saddlebrown",command=c)
button3.grid(row=0,column=3)





#main watch
root.wm_attributes('-topmost',1)
root.mainloop()
