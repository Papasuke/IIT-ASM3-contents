from tkinter import *  
from PIL import ImageTk,Image  

window = Tk()  

window.title(" Memeiacs' image comparison software ")
window.geometry("1920x1080")

canvas = Canvas(window, width = 1500, height = 1600)  
canvas.pack()  

img = ImageTk.PhotoImage(Image.open
    ("snow3.jpg"))  # Paste in the directory, 
                    # example: C:/Users/MDM/Downloads/collection/snow3.jpg

canvas.create_image(20, 20, anchor=NW, image=img) 
window.mainloop()