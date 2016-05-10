import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def clicked(pos):
        print('Button at {0} clicked'.format(pos))
    def createWidgets(self):
        for i in range(10):
            for j in range(10):
                tk.Button(self, text='  ').grid(row=i, column=j)


    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()