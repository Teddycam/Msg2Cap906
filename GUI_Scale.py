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
    selection = window.Selected.get() + ": Attenuation = " + str((window.AttInteger.get())+float(spin.get()))+'dB'
    print(selection)
    print(window.Selected.get())
    print(window.AttInteger.get())
    print(window.AttDecimal.get())
    label.config(text = selection)
    # window.label.set(selection)
def spc():
    """
    Handler for Spinbox vidgets, read values of spinboxes and Scale, Send it to the Label widget for refreshing its value
    :param: none
    :return: none
    """
    selection = window.Selected.get() + ": Attenuation = " + str((window.AttInteger.get())+window.AttDecimal.get())+'dB'
    # print(window.AttDecimal.get())
    label.config(text = selection)
def scp(v):
    """
    Handler for Scale vidget
    :param: v Scale value (String)
    """
    selection = window.Selected.get() + ": Attenuation = " + str((window.AttInteger.get())+window.AttDecimal.get())+'dB'
    selection = window.Selected.get() + ": Attenuation = " + str( float(v) + window.AttDecimal.get())+'dB'
    print(v)
    label.config(text = selection)

window = Tk()
window.AttInteger = DoubleVar()
var11 = StringVar()
window.AttDecimal = DoubleVar()
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
spin = Spinbox(window,
               text="dB",
               width=8,
               from_=0,
               to=0.9,
               increment = 0.1,
               command = spc,
               textvariable = window.AttDecimal,
               wrap=True)
spin2 = Spinbox(frame1,
                values=sorted(ATTs),
                width=8,
                textvariable=window.Selected,
                font='System 8',
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
spin2.pack(side = 'top')
label.pack(side = 'bottom')
scale.pack(anchor = CENTER, side = 'bottom')
frame2.pack(side = 'bottom')
button1.pack(side = 'left')
button2.pack(side = 'right')
spin.pack(side = 'bottom')

window.mainloop()
