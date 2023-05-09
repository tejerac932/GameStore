from tkinter import *
from PIL import ImageTk, Image
# Create a child class of Frame
# This allows us to use Frame method
class Background(Frame):
    def __init__(self, master,img_path):
        # overload frame to have root as the input
        super().__init__(master)


        # opens image
        self.image = Image.open(img_path)
        self.img_copy= self.image.copy()

        # makes image Tk compatible
        self.background_image = ImageTk.PhotoImage(self.image)

        # sets background as image 
        self.background = Label(self, image=self.background_image)
        #determines background location
        self.background.pack(fill=BOTH, expand=YES)
        #adds listener to configure event
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
