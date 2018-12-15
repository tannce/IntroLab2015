from tkinter import *
class Application(Frame):
    """ A GUI application with three buttons. """
    def __init__(self,master):
        """ Initialize the Frame """
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        """ create 3 buttons """
        #first
        self.button1=Button(self,text='This is the first button')
        self.button1.grid()
        
        #second
        self.button2=Button(self)
        self.button2.grid()
        self.button2.configure(text='This is the second button')
        
        #three
        self.button3=Button(self)
        self.button3.grid()
        self.button3['text']='This is the three button'
root=Tk()
root.title('Three Buttons')
root.geometry('350x85')

app=Application(root)

root.mainloop()