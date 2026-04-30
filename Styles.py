import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("1200x800")

s = ttk.Style()
s.theme_use('alt') 

s.configure('Danger.TFrame', background='#e74c3c', borderwidth=5, relief='raised')
s.configure('Safe.TFrame', background='#2ecc71', borderwidth=5, relief='groove')
s.configure('Caution.TFrame', background='#f1c40f', borderwidth=5, relief='ridge')
s.configure('Info.TFrame', background='#3498db', borderwidth=5, relief='sunken')
s.configure('Neutral.TFrame', background="#132223", borderwidth=5, relief='flat')

f1 = ttk.Frame(root, width=150, height=150, style='Danger.TFrame')
f1.grid(row=0, column=0, padx=20, pady=20)
f1.grid_propagate(False)

f2 = ttk.Frame(root, width=150, height=150, style='Safe.TFrame')
f2.grid(row=0, column=1, padx=20, pady=20)
f2.grid_propagate(False)

f3 = ttk.Frame(root, width=150, height=150, style='Caution.TFrame')
f3.grid(row=1, column=0, padx=20, pady=20)
f3.grid_propagate(False)

f4 = ttk.Frame(root, width=150, height=150, style='Info.TFrame')
f4.grid(row=1, column=1, padx=20, pady=20)
f4.grid_propagate(False)

f5 = ttk.Frame(root, width=150, height=150, style='Neutral.TFrame')
f5.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
f5.grid_propagate(False)

root.mainloop()
