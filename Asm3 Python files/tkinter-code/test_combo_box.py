import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime

window = tk.Tk()

# Config the window
window.geometry('800x600')
window.resizable(False, False)
window.title("Memeiacs' combobox testing")

# Label
label = ttk.Label(text="Select a month:")
label.pack(fill=tk.X, padx=20, pady=5)

# Create a combobox
selected_month = tk.StringVar()
month_combobox = ttk.Combobox(window, textvariable=selected_month)

# Display every month in 3 letters 
month_combobox['values'] = [month_name[m][0:3] for m in range(1, 13)]

# Prevent typing a value
month_combobox['state'] = 'readonly'

# Place the widget
month_combobox.pack(fill=tk.X, padx=5, pady=5)


#Bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}!'
    )


month_combobox.bind('<<ComboboxSelected>>', month_changed)

# Displaying the current month
current_month = datetime.now().strftime('%b')
month_combobox.set(current_month)

# Run the application
window.mainloop()