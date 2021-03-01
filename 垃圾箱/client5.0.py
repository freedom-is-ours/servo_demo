import sys  #sysexit结束程序
import socket
import time 
import socket
import tkinter 

HOST = '192.168.1.116' #指服务端IP地址
PORT = 8001  #端口号
window = tkinter.Tk()
window.title('舵机控制中心')
window.geometry('1000x600')

L1 = tkinter.Label(window, text='舵机1(成像舵机)', bg='gray', font=('Arial', 10), width=20, height=2)
L2 = tkinter.Label(window, text='舵机2', bg='gray', font=('Arial', 10), width=20, height=2)
L3 = tkinter.Label(window, text='舵机3', bg='gray', font=('Arial', 10), width=20, height=2)
L4 = tkinter.Label(window, text='舵机4', bg='gray', font=('Arial', 10), width=20, height=2)
L5 = tkinter.Label(window, text='舵机5(532shutter)', bg='gray', font=('Arial', 10), width=20, height=2)
L6 = tkinter.Label(window, text='舵机6(离子化shutter)', bg='gray', font=('Arial', 10), width=20, height=2)
L7 = tkinter.Label(window, text='舵机7', bg='gray', font=('Arial', 10), width=20, height=2)
L8 = tkinter.Label(window, text='舵机8', bg='gray', font=('Arial', 10), width=20, height=2)


scrollbar = tkinter.Scrollbar(window)
scrollbar.pack(side='right',fill = 'y')
listbox = tkinter.Listbox(window,width = 30, yscrollcommand=scrollbar.set)

# for i in range(100):
#     listbox.insert('end','设置舵机1为'+str(i))


v1 = tkinter.IntVar()
def eventHandler1():
    #print(v1.get())
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    sock1.send(b'4')
    sock1.close()
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    if v1.get() == 0:
        sock1.send(b'0')
        sock1.close()
    if v1.get() == 45:
        sock1.send(b'1')
        sock1.close()
    if v1.get() == 90:
        sock1.send(b'2')
        sock1.close()
    if v1.get() == 135:
        sock1.send(b'3')
        sock1.close()        
    listbox.insert('end','设置舵机1为'+str(v1.get())+'度')
L1_btn1 = tkinter.Radiobutton(window, text="0",bg='white', width=10, height=2,variable=v1, value=0,command = eventHandler1)
L1_btn2 = tkinter.Radiobutton(window, text="45",bg='white', width=10, height=2,variable=v1, value=45,command = eventHandler1)
L1_btn3 = tkinter.Radiobutton(window, text="90",bg='white', width=10, height=2,variable=v1, value=90,command = eventHandler1)
L1_btn4 = tkinter.Radiobutton(window, text="135",bg='white', width=10, height=2,variable=v1, value=135,command = eventHandler1)

v2 = tkinter.IntVar()
def eventHandler2():
    #print(v2.get())
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    sock1.send(b'6')
    sock1.close()
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    if v2.get() == 0:
        sock1.send(b'0')
        sock1.close()
    if v2.get() == 45:
        sock1.send(b'1')
        sock1.close()
    if v2.get() == 90:
        sock1.send(b'2')
        sock1.close()
    if v2.get() == 135:
        sock1.send(b'3')
        sock1.close()        
    listbox.insert('end','设置舵机2为'+str(v2.get())+'度')
L2_btn1 = tkinter.Radiobutton(window, text="0",bg='white', width=10, height=2,variable=v2, value=0,command = eventHandler2)
L2_btn2 = tkinter.Radiobutton(window, text="45",bg='white', width=10, height=2,variable=v2, value=45,command = eventHandler2)
L2_btn3 = tkinter.Radiobutton(window, text="90",bg='white', width=10, height=2,variable=v2, value=90,command = eventHandler2)
L2_btn4 = tkinter.Radiobutton(window, text="135",bg='white', width=10, height=2,variable=v2, value=135,command = eventHandler2)

v3 = tkinter.IntVar()
def eventHandler3():
    #print(v3.get())
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    sock1.send(b'8')
    sock1.close()
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    if v3.get() == 0:
        sock1.send(b'0')
        sock1.close()
    if v3.get() == 45:
        sock1.send(b'1')
        sock1.close()
    if v3.get() == 90:
        sock1.send(b'2')
        sock1.close()
    if v3.get() == 135:
        sock1.send(b'3')
        sock1.close() 
    listbox.insert('end','设置舵机3为'+str(v3.get())+'度')
L3_btn1 = tkinter.Radiobutton(window, text="0",bg='white', width=10, height=2,variable=v3, value=0,command = eventHandler3)
L3_btn2 = tkinter.Radiobutton(window, text="45",bg='white', width=10, height=2,variable=v3, value=45,command = eventHandler3)
L3_btn3 = tkinter.Radiobutton(window, text="90",bg='white', width=10, height=2,variable=v3, value=90,command = eventHandler3)
L3_btn4 = tkinter.Radiobutton(window, text="135",bg='white', width=10, height=2,variable=v3, value=135,command = eventHandler3)

v4 = tkinter.IntVar()
def eventHandler4():
    #print(v4.get())
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    sock1.send(b'10')
    sock1.close()
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    if v4.get() == 0:
        sock1.send(b'0')
        sock1.close()
    if v4.get() == 45:
        sock1.send(b'1')
        sock1.close()
    if v4.get() == 90:
        sock1.send(b'2')
        sock1.close()
    if v4.get() == 135:
        sock1.send(b'3')
        sock1.close() 
    listbox.insert('end','设置舵机4为'+str(v4.get())+'度')
L4_btn1 = tkinter.Radiobutton(window, text="0",bg='white', width=10, height=2,variable=v4, value=0,command = eventHandler4)
L4_btn2 = tkinter.Radiobutton(window, text="45",bg='white', width=10, height=2,variable=v4, value=45,command = eventHandler4)
L4_btn3 = tkinter.Radiobutton(window, text="90",bg='white', width=10, height=2,variable=v4, value=90,command = eventHandler4)
L4_btn4 = tkinter.Radiobutton(window, text="135",bg='white', width=10, height=2,variable=v4, value=135,command = eventHandler4)

v5 = tkinter.IntVar()
def eventHandler5():
    #print(v5.get())
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    sock1.send(b'12')
    sock1.close()
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    if v5.get() == 0:
        sock1.send(b'0')
        sock1.close()
    if v5.get() == 45:
        sock1.send(b'1')
        sock1.close()
    if v5.get() == 90:
        sock1.send(b'2')
        sock1.close()
    if v5.get() == 135:
        sock1.send(b'3')
        sock1.close() 
    listbox.insert('end','设置舵机5为'+str(v5.get())+'度')
L5_btn1 = tkinter.Radiobutton(window, text="0",bg='white', width=10, height=2,variable=v5, value=0,command = eventHandler5)
L5_btn2 = tkinter.Radiobutton(window, text="45",bg='white', width=10, height=2,variable=v5, value=45,command = eventHandler5)
L5_btn3 = tkinter.Radiobutton(window, text="90",bg='white', width=10, height=2,variable=v5, value=90,command = eventHandler5)
L5_btn4 = tkinter.Radiobutton(window, text="135",bg='white', width=10, height=2,variable=v5, value=135,command = eventHandler5)

v6 = tkinter.IntVar()
def eventHandler6():
    #print(v6.get())
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    sock1.send(b'14')
    sock1.close()
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    if v6.get() == 0:
        sock1.send(b'0')
        sock1.close()
    if v6.get() == 45:
        sock1.send(b'1')
        sock1.close()
    if v6.get() == 90:
        sock1.send(b'2')
        sock1.close()
    if v6.get() == 135:
        sock1.send(b'3')
        sock1.close() 
    listbox.insert('end','设置舵机6为'+str(v6.get())+'度')
L6_btn1 = tkinter.Radiobutton(window, text="0",bg='white', width=10, height=2,variable=v6, value=0,command = eventHandler6)
L6_btn2 = tkinter.Radiobutton(window, text="45",bg='white', width=10, height=2,variable=v6, value=45,command = eventHandler6)
L6_btn3 = tkinter.Radiobutton(window, text="90",bg='white', width=10, height=2,variable=v6, value=90,command = eventHandler6)
L6_btn4 = tkinter.Radiobutton(window, text="135",bg='white', width=10, height=2,variable=v6, value=135,command = eventHandler6)

v7 = tkinter.IntVar()
def eventHandler7():
    #print(v7.get())
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    sock1.send(b'16')
    sock1.close()
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    if v7.get() == 0:
        sock1.send(b'0')
        sock1.close()
    if v7.get() == 45:
        sock1.send(b'1')
        sock1.close()
    if v7.get() == 90:
        sock1.send(b'2')
        sock1.close()
    if v7.get() == 135:
        sock1.send(b'3')
        sock1.close() 
    listbox.insert('end','设置舵机7为'+str(v7.get())+'度')
L7_btn1 = tkinter.Radiobutton(window, text="0",bg='white', width=10, height=2,variable=v7, value=0,command = eventHandler7)
L7_btn2 = tkinter.Radiobutton(window, text="45",bg='white', width=10, height=2,variable=v7, value=45,command = eventHandler7)
L7_btn3 = tkinter.Radiobutton(window, text="90",bg='white', width=10, height=2,variable=v7, value=90,command = eventHandler7)
L7_btn4 = tkinter.Radiobutton(window, text="135",bg='white', width=10, height=2,variable=v7, value=135,command = eventHandler7)

v8 = tkinter.IntVar()
def eventHandler8():
    #print(v8.get())
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    sock1.send(b'18')
    sock1.close()
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((HOST,PORT))
    if v8.get() == 0:
        sock1.send(b'0')
        sock1.close()
    if v8.get() == 45:
        sock1.send(b'1')
        sock1.close()
    if v8.get() == 90:
        sock1.send(b'2')
        sock1.close()
    if v8.get() == 135:
        sock1.send(b'3')
        sock1.close() 
    listbox.insert('end','设置舵机8为'+str(v8.get())+'度')
L8_btn1 = tkinter.Radiobutton(window, text="0",bg='white', width=10, height=2,variable=v8, value=0,command = eventHandler8)
L8_btn2 = tkinter.Radiobutton(window, text="45",bg='white', width=10, height=2,variable=v8, value=45,command = eventHandler8)
L8_btn3 = tkinter.Radiobutton(window, text="90",bg='white', width=10, height=2,variable=v8, value=90,command = eventHandler8)
L8_btn4 = tkinter.Radiobutton(window, text="135",bg='white', width=10, height=2,variable=v8, value=135,command = eventHandler8)



L1.place(x = 10, y = 10)
L1_btn1.place(x = 40 , y = 80, anchor = 'w')
L1_btn2.place(x = 40 , y = 140, anchor = 'w')
L1_btn3.place(x = 40 , y = 200, anchor = 'w')
L1_btn4.place(x = 40 , y = 260, anchor = 'w')

L2.place(x = 210 ,y = 10)
L2_btn1.place(x = 240 , y = 80, anchor = 'w')
L2_btn2.place(x = 240 , y = 140, anchor = 'w')
L2_btn3.place(x = 240 , y = 200, anchor = 'w')
L2_btn4.place(x = 240 , y = 260, anchor = 'w')

L3.place(x = 410 ,y = 10)
L3_btn1.place(x = 440 , y = 80, anchor = 'w')
L3_btn2.place(x = 440 , y = 140, anchor = 'w')
L3_btn3.place(x = 440 , y = 200, anchor = 'w')
L3_btn4.place(x = 440 , y = 260, anchor = 'w')

L4.place(x = 610 ,y = 10)
L4_btn1.place(x = 640 , y = 80, anchor = 'w')
L4_btn2.place(x = 640 , y = 140, anchor = 'w')
L4_btn3.place(x = 640 , y = 200, anchor = 'w')
L4_btn4.place(x = 640 , y = 260, anchor = 'w')

L5.place(x = 10, y = 310)
L5_btn1.place(x = 40 , y = 380, anchor = 'w')
L5_btn2.place(x = 40 , y = 440, anchor = 'w')
L5_btn3.place(x = 40 , y = 500, anchor = 'w')
L5_btn4.place(x = 40 , y = 560, anchor = 'w')

L6.place(x = 210 ,y = 310)
L6_btn1.place(x = 240 , y = 380, anchor = 'w')
L6_btn2.place(x = 240 , y = 440, anchor = 'w')
L6_btn3.place(x = 240 , y = 500, anchor = 'w')
L6_btn4.place(x = 240 , y = 560, anchor = 'w')

L7.place(x = 410 ,y = 310)
L7_btn1.place(x = 440 , y = 380, anchor = 'w')
L7_btn2.place(x = 440 , y = 440, anchor = 'w')
L7_btn3.place(x = 440 , y = 500, anchor = 'w')
L7_btn4.place(x = 440 , y = 560, anchor = 'w')

L8.place(x = 610 ,y = 310)
L8_btn1.place(x = 640 , y = 380, anchor = 'w')
L8_btn2.place(x = 640 , y = 440, anchor = 'w')
L8_btn3.place(x = 640 , y = 500, anchor = 'w')
L8_btn4.place(x = 640 , y = 560, anchor = 'w')

listbox.pack(side='right',anchor = 'w',fill = 'y')
 
scrollbar.config(command=listbox.yview)

window.mainloop()
