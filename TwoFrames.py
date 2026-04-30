import tkinter as tk

root = tk.Tk() 
root.geometry("1200x750")

sidebar = tk.Frame(root, bg="#31485e", width=200)
#use bg="#31485e" then pwede kayo maglagay ng color code para sa background color ng frame, at yung width para sa lapad ng frame
#pero sa vs code and pycharm lang ito kasi sa ibang IDEs like jupyter notebook, hindi siya nag aaccept ng color code kaya kailangan natin gumamit ng color name like "blue" or "red" para sa background color
sidebar.pack(side="left", fill="y")
#side="left" para sa left side ng window, at fill="y" para mag stretch siya sa y axis pero hindi sa x axis kaya hindi siya mag stretch sa buong width ng window
labels = tk.Label(sidebar, text="Hi, I'm a person", bg="#31485e", fg="white", font=("Arial", 18))
labels.pack(side="bottom", pady=10)

top_frame = tk.Frame(root, bg="violet", relief="sunken", borderwidth=10 ) 
top_frame.pack(side="top", fill="x")

label = tk.Label(top_frame, text="This is a Frame!", bg="blue", fg="white", font=("Arial", 24)) 
label.pack(pady=10)

root.mainloop()
