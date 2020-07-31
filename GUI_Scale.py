from tkinter import *

def p2():
    """
    Handler for right Button vidget ( ' Cancel', destroy tk window, cancel program execution
    :param: none
    :return: none
    """
    print('Key2 pressed')
    window.destroy()
    exit(0)
def p1():
    """
    Handler for Left Button vidget, read values of spinboxes and Scale, Send it to the Label widget for refreshing its value
    :param: none
    :return: none
    """
    selection = window.Selected.get() + ": Attenuation = " + str((window.AttInteger.get())+window.AttDecimal.get()/10)+'dB'
    print(selection)
    print(window.Selected.get())
    Att = window.AttInteger.get()+window.AttDecimal.get()/10
    print('Value = ',Att)
    label.config(text = selection)
    # window.label.set(selection)

def spc():
    """
    Handler for Spinbox vidgets, read values of spinboxes and Scale, Send it to the Label widget for refreshing its value
    :param: none
    :return: none
    """
    window.AttInteger.set(window.AttDecs.get()*10+window.AttOnes.get())
    selection = window.Selected.get() + ": Attenuation = " + str((window.AttInteger.get())+window.AttDecimal.get()/10)+'dB'
    # print(window.AttDecimal.get())
    label.config(text = selection)

def scp(v):
    """
    Handler for Scale vidget
    :param: v Scale value (String)
    """
    window.AttOnes.set(int(window.AttInteger.get() % 10)) # единицы = остаток от деления на 10
    window.AttDecs.set(int(window.AttInteger.get() // 10)) # Десятки = результат целочисленного деления на 10
    selection = window.Selected.get() + ": Attenuation = " + str((window.AttInteger.get())+window.AttDecimal.get()/10)+'dB'
    selection = window.Selected.get() + ": Attenuation = " + str( float(v) + window.AttDecimal.get()/10)+'dB'
    # print(v)
    label.config(text = selection)

window = Tk()
window.AttInteger = DoubleVar()
var11 = StringVar()
window.AttDecimal = DoubleVar()
window.AttOnes = IntVar()
window.AttDecs = IntVar()
window.Selected = StringVar()
ATTs = ('Att #01', 'Att #02', 'Att #03', 'Att #04', 'Att #05', 'Att #06', 'Att #07', 'Att #08', 'Att #09', 'Att #10', 'Att #11', 'Att #12')

window.title("Attenuation")

frame1 = Frame(window,
               background = 'white',
               bd = 2)
frame2 = Frame(window,
               background = 'white',
               bd = 2)
label = Label(frame1,
              foreground = "#010",
              background = 'white',
              font = 'System 8',
              text = 'dB')
spw = LabelFrame (window, bd = 2, fg = 'blue', text = 'Select attenuation:')
spin = Spinbox(spw,
               text="0.1 dB",
               width=1,
               from_=0,
               to=9,
               increment = 1,
               format='%1.1f',
               font='System 6',
               command = spc,
               textvariable = window.AttDecimal,
               wrap=True)
spin1 = Spinbox(spw,
               text="1 dB",
               width=1,
               from_=0,
               to=9,
               increment = 1,
               # format='%1s',
               font='System 9',
               command = spc,
               textvariable = window.AttOnes,
               wrap=True)
labelPoint = Label(spw,
              foreground = "#010",
              background = 'white',
              font = 'System 10',
              text = '.')
spin10 = Spinbox(spw,
               text="10 dB",
               width=1,
               from_=0,
               to=6,
               increment = 1,
               # format='%1f',
               font='System 10',
               command = spc,
               textvariable = window.AttDecs,
               wrap=True)
spinLab = Spinbox(frame1,
                values=sorted(ATTs),
                width=8,
                textvariable=window.Selected,
                font='System 9',
                command = spc,
                wrap=True)
scale = Scale(frame1,
              background = 'white',
              highlightbackground = '#D0E0FF',
              activebackground = 'blue',
              font = 'Tahoma 8',
              digits = 2,
              variable = window.AttInteger,
              orient = HORIZONTAL,
              to = 63,
              length = 300,
              sliderrelief = SUNKEN,
              relief = FLAT,
              label = 'dB',
              tickinterval = 5,
              troughcolor = '#D0E0FF',
              showvalue = 1,
              command=scp,
              sliderlength = 36,
              width = 30)

button1 = Button(frame2,text = 'SET',
                        # background = "#999",  # фоновый цвет кнопки
                        activebackground= "#999",
                        foreground = "#010",  # цвет текста
                        padx = "5",  # отступ от границ до содержимого по горизонтали
                        pady = "4",  # отступ от границ до содержимого по вертикали
                        font='System 8',
                        # font = "9",  # высота шрифта
                        command=p1)
button2 = Button(frame2, text = 'Cancel',
                         background="#777",  # фоновый цвет кнопки
                         foreground="#000",  # цвет текста
                         padx="5",  # отступ от границ до содержимого по горизонтали
                         pady="4",  # отступ от границ до содержимого по вертикали
                         font='System 8',
                         # font="9",  # высота шрифта
                         command = p2)

frame1.pack(side = 'top')
spinLab.pack(side = 'top')
label.pack(side = 'bottom')
scale.pack(anchor = CENTER, side = 'bottom')
frame2.pack(side = 'bottom')
button1.pack(side = 'left')
button2.pack(side = 'right')
spw.pack(side = 'bottom')
spin10.pack(side = 'left')
spin1.pack(side = 'left')
labelPoint.pack(side = 'left')
spin.pack(side = 'left')
window.mainloop()
