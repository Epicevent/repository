import tkinter
import naverapi
from PIL import ImageTk

class Map:
  def  __init__(self):
      self.XYstring = "126.8397859,37.4991205"
      self.rootsizeString = '1000x1000'
      self.root = tkinter.Tk()
      self.Initialize()

  def Initialize(self):
      self.root.geometry('1000x1000')
      self.menubar = tkinter.Menu(self.root)
      menu_1 = tkinter.Menu(self.menubar, tearoff=0)
      menu_1.add_command(label="하위 메뉴 1-1")
      menu_1.add_command(label="하위 메뉴 1-2")
      menu_1.add_separator()
      menu_1.add_command(label="하위 메뉴 1-3")
      self.root.config(menu=self.menubar)
      self.canvas = tkinter.Canvas(self.root, width=640, height=640)
      self.canvas.pack()
      self.drawMap(XYstring=self.getXYstring())
  def getXYstring(self):
      return self.XYstring
  def drawMap(self,XYstring,level=14):
      pilImage = naverapi.staticmap(XYstring, level=level)
      image = ImageTk.PhotoImage(pilImage)
      self.canvas.create_image(320, 320, image=image)
      self.root.mainloop()
if __name__ == '__main__':
    myMap = Map()
    myMap.drawMap(XYstring='127.0097859,37.4991205',level=1)