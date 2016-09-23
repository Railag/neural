from tkinter.filedialog import *
from tkinter import *
import PIL.Image, PIL.ImageTk

from neural.network import Network
from neural.neuron import Neuron


def quit(ev):
    global root
    root.destroy()


def teach(ev):
    w0 = int(wText.get("1.0", END))

    network.setup_w0(w0)

    network.teach(teach_callback)


def teach_callback(neuron):
    textbox.insert('1.0', neuron.get_matrix())


def load_file(ev):
    fn = Open(root, filetypes=[('*.bmp files', '.bmp')]).show()
    if fn == '':
        return

    img, result = network.handle_file(fn)

    canvas.background = PIL.ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=canvas.background, anchor="nw")

    textbox.insert('1.0', "\n")
    textbox.insert('1.0', "Neuron with " + result.neuron.letter.upper() + " letter")
    textbox.insert('1.0', "\n")
    textbox.insert('1.0', "Valid = " + str(result.result))
    textbox.insert('1.0', "\n")
    textbox.insert('1.0', "Sum = " + str(result.sum))
    textbox.insert('1.0', "\n")


root = Tk()

width = 5
height = 8

network = Network(width, height)

panelFrame = Frame(root, height=60, bg='gray')
imageFrame = Frame(root, height=80, width=50, bg='red')
textFrame = Frame(root, height=34, width=60)
image2Frame = Frame(root, height=200)

panelFrame.pack(side='top', fill='both')
image2Frame.pack()
textFrame.pack()

textbox = Text(textFrame, font='Arial 14', wrap='word')

imagebox = PhotoImage()

canvas = Canvas(image2Frame, height=200)
canvas.pack(side="bottom", fill="both", expand="yes")

wText = Text(image2Frame, height=1, width=4, wrap='word')
wText.insert("1.0", 'w')
wText.pack()

textbox.pack()

startBtn = Button(panelFrame, text='Teach')
loadBtn = Button(panelFrame, text='Load')
quitBtn = Button(panelFrame, text='Quit')

startBtn.bind("<Button-1>", teach)
loadBtn.bind("<Button-1>", load_file)
quitBtn.bind("<Button-1>", quit)

loadBtn.place(x=10, y=10, width=40, height=40)
quitBtn.place(x=110, y=10, width=40, height=40)
startBtn.place(x=60, y=10, width=40, height=40)

root.mainloop()
