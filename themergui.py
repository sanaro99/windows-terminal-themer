import themer as th
from tkinter import *
from tkcolorpicker import askcolor

root = Tk()

# def acryOpcty():
#     th.currentProf['acrylicOpacity'] = opcty.get()
#     th.writeProfile(th.currentProf)

# def cursorShape():
#     th.currentProf['cursorShape'] = str(curshape.get())
#     # print(th.currentProf)
#     th.writeProfile(th.currentProf)

def unifiedWrite(profName, val):
    th.currentProf[profName] = val
    th.writeProfile(th.currentProf)

def pickColor(profName):
    bgcolor.set(askcolor(bgcolor.get(), root)[1])
    unifiedWrite(profName, bgcolor.get())



# Define variables
opcty = DoubleVar(value=th.currentProf['acrylicOpacity'])
curshape = StringVar(value=th.currentProf['cursorShape'])
bgcolor = StringVar(value=th.currentProf['background'])

cursorShapeList = [
    'bar',
    'emptyBox',
    'filledBox',
    'underscore',
    'vintage'
]


# Frame
LabelFrame(root, text='Windows Terminal Themer',padx=5, pady=6).grid(padx=5, pady=5)

# Acrylic Opacity
Label(root, text='Acrylic Opacity').grid()
acryOpctyScale = Scale(root, variable = opcty, orient = HORIZONTAL, from_ = 0, resolution = 0.01, to = 1.0)
acryOpctyScale.grid(column = 0)
acryOpctyBttn = Button(root, text = 'Set', command=lambda: unifiedWrite('acrylicOpacity', opcty.get()))
acryOpctyBttn.grid(column = 1)

# Cursor Shape
Label(root, text='Cursor Shape').grid()
for i in range(len(cursorShapeList)):
    R = Radiobutton(root, text=cursorShapeList[i], variable=curshape, value=cursorShapeList[i], command=lambda: unifiedWrite('cursorShape', curshape.get()))
    R.grid()
    
# Background Color
Label(root, text='Background Color').grid()
Button(root, text='Color Picker', command=lambda: pickColor('background')).grid()


root.mainloop()