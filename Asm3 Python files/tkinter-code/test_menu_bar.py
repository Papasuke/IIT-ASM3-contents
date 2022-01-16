import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#DEFINE A WINDOW
window=tk.Tk()
window.title(" Memeiacs' image comparison software ")
window.geometry("800x600")
newlabel = tk.Label(text = " Trust and use our image comparison tool, you will not regret seeing how it can wind up your image review day ")
newlabel.grid(column=0,row=0)


# DEFINE A MENU BAR
menubar = Menu(window) 

# CREATE "FILE" OPTION AND ADD FOLLOWING COMMANDS FOR TESTING
file = Menu(menubar, tearoff=1) 
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as")    
file.add_separator()  
file.add_command(label="Exit", command=window.quit)  
menubar.add_cascade(label="File", menu=file)  

# CREATE "EDIT" OPTION AND ADD FOLLOWING COMMANDS FOR TESTING
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
# edit.add_separator()     
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  

# CREATE "LIBRARY" OPTION FOR TESTING
library = Menu(menubar, tearoff=0) 
menubar.add_cascade(label="Library", menu=library) 

# CREATE "TOOL" OPTION FOR TESTING
tool = Menu(menubar, tearoff=0) 
menubar.add_cascade(label="Tool", menu=tool)

# CREATE "VIEW" OPTION FOR TESTING
view = Menu(menubar, tearoff=0) 
menubar.add_cascade(label="View", menu=view)  
    
window.config(menu=menubar)



#RUN THE APPLICATION
window.mainloop()
