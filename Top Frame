import tkinter as tk

root = tk.Tk() #Siyan yung gumagawa ng window
root.geometry("1200x750") #This is the window size

top_frame = tk.Frame(root, bg="green",relief="sunken", borderwidth=10 ) 
# yung tk.frame siya yung nag aallowed na lagyan ng mga style yung frame, yung bg para sa background color,- 
# yung relief para sa border style, at yung borderwidth para sa kapal ng border para mas lalong maging malalim na frame kasi sunken yung pinili natin na relief
top_frame.pack(side="top", fill="x")
#.pack siya yung nagstyle kung saan si frame na mapupunta sa window, yung side para sa kung saan mapupunta yung frame, at yung fill siya yung magstretch, sa x axis siya magstretch kaya fill="x"

label = tk.Label(top_frame, text="This is a Frame!", bg="blue", fg="pink", font=("Arial", 24, "bold")) 
#tk.label siya yung nag aallowed na lagyan ng mga style yung label, yung text para sa text na lalabas sa label, yung bg para sa background color, at yung font para sa font style at size
label.pack(side="left", pady=10)
#.pack siya yung nagstyle kung saan si label na mapupunta sa frame, yung pady para sa padding sa y axis para hindi dumikit sa edges ng frame or sa mga ibang label sa loon ng frame


root.mainloop()
# This is the main loop that keeps the window open and responsive to user interactions.
