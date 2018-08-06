import tkinter as tk
from tkinter import filedialog

# this class is an instance of a Frame. It is not required to do it this way.
# this is just my preferred method.
class ReadFile(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        # we need to make sure that this instance of tk.Frame is visible.
        self.pack()
        # create Button that link to methods used to get file path.
        tk.Button(self, text="Open file", command=self.open_and_prep).pack()
        # create Button that link to methods used to process said file.
        tk.Button(self, text="Print Content", command=self.process_open_file).pack()

    def open_and_prep(self):
        # askopefilename is used to retrieve the file path and file name.
        self.file_path = filedialog.askopenfilename()

    def process_open_file(self):
        # do what you want with the file here.
        if self.file_path != "":
            # opens file from file path and prints each line.
            with open(self.file_path,"r") as testr:
                for line in testr:
                    print (line)

if __name__ == "__main__":
    # tkinter requires one use of Tk() to start GUI
    root = tk.Tk()
    TestApp = ReadFile()
    # tkinter requires one use of mainloop() to manage the loop and updates of the GUI
    root.mainloop()