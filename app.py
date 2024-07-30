from tkinter import*
from tkinter.constants import CENTER, LEFT, RIDGE, RIGHT, TOP

window = Tk()

window.geometry("480x320")

window.resizable(0, 0)

window.title("Emotion Detection")
#background
background = PhotoImage(file="image.png")

label1 = Label( window, image = background)
label1.place(x = -100, y = -100)

#include face dection
def OpenFaceDection():
    import face    
    face.start()
#include face dection    

btn1 = Button(text="Face detection", bg='#B0AA9C',command=OpenFaceDection)

btn1.pack(side=LEFT,padx=190)

window.mainloop()