from tkinter import *
# import tkinter
# import tkinter.filedialog
# import tkinter
# from tkinter import *
# from tkinter import Tk, BOTH, IntVar, LEFT
# from ttk import Frame, Label, Scale, Style

def ppp(event):
    print('Key1 pressed', file=sys.stdout)
def p1():
    print('Key1 pressed')
    tt = text1.get('1.0', END)
    print (tt)
    vv.append(var1.get())
    vv.append(var2.get())
    vv.append(var3.get())
    vv.append(var4.get())
    vv.append(var5.get())
    vv.append(var6.get())
    vv.append(var7.get())
    vv.append(var8.get())
    vv.append(var9.get())
    print(vv)
    for i in vv:
        print(i)
    print(listbox1.curselection())

def eee(event):
    print('Key2 pressed')
    exit(0)
def p2():
    print('Key2 pressed')
    window.destroy()
    # exit(0)
def c0():
    print('1.Checked ', var1.get(),' | Radio = ', var9.get())

def sel():
   selection = "Value = " + str(var10.get())
   print(selection)
   label.config(text = selection)

window = Tk()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = DoubleVar()
var11 = IntVar()
# var10 = IntVar()
# var11 = IntVar()
vv = []
window.title("Attenuation")
# text1 = Text(window, height = 2, width = 14, font = 'Arial 14', wrap = WORD)
# listbox1 = Listbox(window, height = 8, width = 15, selectmode = EXTENDED)
# text1.insert(1.0, 'Текстовый текст')
# list1 = ['Выбор №0','Выбор №1','Выбор №2','Выбор №3','Выбор №4','Выбор №5','Выбор №6','Выбор №7','Выбор №8','Выбор №9', 'Выбор №10','Выбор №11']
# for i in list1: listbox1.insert(END,i)
# check1 = Checkbutton(frame2, text = '1 пункт', variable = var1,
#                      onvalue = True, offvalue = False,command = c0)
# check2 = Checkbutton(frame2, text = '2 пункт', variable = var2, onvalue = 1, offvalue = 0)
# check3 = Checkbutton(frame2, text = '3 пункт', variable = var3, onvalue = 1, offvalue = 0)
# check4 = Checkbutton(frame2, text = '4 пункт', variable = var4, onvalue = 1, offvalue = 0)
# check5 = Checkbutton(frame2, text = '5 пункт', variable = var5, onvalue = 1, offvalue = 0)
# check6 = Checkbutton(frame2, text = '6 пункт', variable = var6, onvalue = 1, offvalue = 0)
# check7 = Checkbutton(frame2, text = '7 пункт', variable = var7, onvalue = 1, offvalue = 0)
# check8 = Checkbutton(frame2, text = '8 пункт', variable = var8, onvalue = 1, offvalue = 0)
# rbutton1 = Radiobutton( window, text = 'Screen', variable = var9, value = 1, command = c0)
# rbutton2 = Radiobutton( window, text = 'Text file', variable = var9, value = 2, command = c0)
# rbutton3 = Radiobutton( window, text = 'XLS file', variable = var9, value = 3, command = c0)
frame1 = Frame(window, background = 'white', bd = 2)
frame2 = Frame(window, background = 'black', bd = 2)
label = Label(frame1, foreground = "#010")

scale = Scale(frame1, variable = var10, orient = HORIZONTAL, to = 63, length = 300, relief = FLAT, label = 'dB')

button1 = Button(frame2, text = 'SET',
        # background = "#999",  # фоновый цвет кнопки
        activebackground= "#999",
        foreground = "#010",  # цвет текста
        padx = "5",  # отступ от границ до содержимого по горизонтали
        pady = "4",  # отступ от границ до содержимого по вертикали
        font = "10",  # высота шрифта
        command=sel)
button2 = Button(frame2, text = 'Cancel',
         background="#777",  # фоновый цвет кнопки
         foreground="#000",  # цвет текста
         padx="5",  # отступ от границ до содержимого по горизонтали
         pady="4",  # отступ от границ до содержимого по вертикали
         font="10",  # высота шрифта
         command = p2)
# text1.pack(side = 'top', fill = 'both')
# listbox1.pack(side = 'right', fill = 'y', expand = TRUE)
frame1.pack(side = 'top')
scale.pack(anchor = CENTER)
label.pack(side = 'left')

frame2.pack(side = 'bottom')
button1.pack(side = 'left')
button2.pack(side = 'right')
# check1.pack(side = 'top')
# check2.pack(side = 'top')
# check3.pack(side = 'top')
# check4.pack(side = 'top')
# check5.pack(side = 'top')
# check6.pack(side = 'top')
# check7.pack(side = 'top')
# check8.pack(side = 'top')
# rbutton1.pack( fill = 'both', expand = TRUE)
# rbutton2.pack(fill = 'y', expand = TRUE)
# rbutton3.pack(fill = 'y', expand = TRUE)
# button1.bind('<Button-1>',ppp)
# button2.bind('<Button-1>',eee)
window.mainloop()
print('Finished')