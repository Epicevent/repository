from tkinter import *
import naverapi
from PIL import ImageTk
from threading import Lock


class App:

    def __init__(self, master):
        master.option_add('*tearOff', FALSE)
        frame = Frame(master)
        master.geometry("1000x800")
        frame.pack()
        self.lock = Lock()# to sync drawing Map
        self.XYstring = "126.8397859,37.4991205"
        self.xyStrToxyfloats()
        self.displaylevel = 12
        self.naverMapCanvas = Canvas(frame,width=640, height=640)
        self.naverMapCanvas.pack()
        self.naverMapCanvas.bind("<Button-1>", self.xy)
        self.naverMapCanvas.bind("<B1-Motion>", self.moveMap)
        self.naverMapCanvas.bind("<MouseWheel>",self.zoomMap)
        self.lastx, self.lasty = 0, 0
        menu = Menu(master)
        master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Map", menu=filemenu)
        filemenu.add_command(label="drawMap", command=self.drawMap)
        filemenu.add_command(label="Open...", command=callback)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=callback)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="XY좌표", command=self.xyStrToxyfloats)
        helpmenu.add_command(label="DisLevel", command=lambda :print(str(self.displaylevel)))


    def xyStrToxyfloats(self):
        xstr =self.XYstring[0:self.XYstring.index(',')]
        ystr =self.XYstring[self.XYstring.index(',')+1:self.XYstring.__len__()]
        print(xstr+" "+ystr)
        self.Xcoord= float(xstr)
        self.Ycoord= float(ystr)
    def drawMap(self):
        self.lock.acquire()
        self.pilImage = naverapi.staticmap(self.XYstring,self.displaylevel)

        self.MapImage = ImageTk.PhotoImage(self.pilImage)
        self.naverMapCanvas.create_image(320, 320, image=self.MapImage)
        self.lock.release()
    def xy(self,event):
        self.lastx, self.lasty = event.x, event.y

    def moveMap(self,event):
        dxdy=(self.lastx-event.x , event.y - self.lasty)
        newx=self.CaculateNewXY(dxdy)[0]
        newy=self.CaculateNewXY(dxdy)[1]
        self.XYstring=str(newx) + ',' + str(newy)

        self.drawMap()

        self.lastx, self.lasty = event.x, event.y
    def CaculateNewXY(self,dxdy):
        self.xyStrToxyfloats()
        newx=self.Xcoord + pow(2,-self.displaylevel)*dxdy[0]*0.04625
        newy=self.Ycoord + pow(2,-self.displaylevel)*dxdy[1]*0.0375
        return (newx,newy)
    def zoomMap(self,event):
        self.xyStrToxyfloats()
        dxdy = (event.x-320,  320-event.y)
        mouseCoordx = self.CaculateNewXY(dxdy)[0]
        mouseCoordy = self.CaculateNewXY(dxdy)[1]
        if (event.delta>0 ):
            self.displaylevel = naverapi.displayLevel(self.displaylevel + 1)
            self.XYstring = str((self.Xcoord + mouseCoordx)/2) + ',' + str((self.Ycoord + mouseCoordy)/2)
        else:
            self.displaylevel = naverapi.displayLevel(self.displaylevel - 1)
            self.XYstring = str(2 * self.Xcoord - mouseCoordx) + ',' + str(2 * self.Ycoord - mouseCoordy)

        self.drawMap()

def callback():
            print("called the callback!")

root = Tk()

app = App(root)
app.drawMap()
root.mainloop()
