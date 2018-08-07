import tkinter
import naverapi
from PIL import ImageTk
root = tkinter.Tk()
root.geometry('1000x1000')
canvas = tkinter.Canvas(root,width=999,height=999)
canvas.pack()
pilImage = naverapi.staticmap("126.8397859,37.4991205",level=14)
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(400,400,image=image)
root.mainloop()