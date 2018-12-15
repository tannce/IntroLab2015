from tkinter import *
class Application(Frame):
    """ A GUI application with three buttons. """
    def __init__(self,master):
        """ Initialize the Frame """
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks=0
        self.create_widgets()
        
    def create_widgets(self):
        """ create buttons displays number of clicks """
        
        self.button=Button(self)
        self.button['text']='Total Clicks: 0'
        self.button['command']=self.update_count
        self.button.grid()
    def update_count(self):
        """ count click """
        self.button_clicks+=1
        self.button['text']='Total Clicks:'+str(self.button_clicks)

root=Tk()
root.title('Clicks')
root.geometry('350x85')

app=Application(root)

root.mainloop()