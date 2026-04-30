import tkinter as tk

root = tk.Tk()
root.geometry("1200x750")

top_frame = tk.Frame(root, bg="violet", relief="sunken", borderwidth=10, width=400, height=100)
top_frame.pack(expand=True, fill="x")
#kapag gumamit tayo ng expand=true ay mapupunta ito sa gitna ng window, at kapag gumamit tayo ng fill="x" ay magstretch ito sa x axis pero hindi sa y axis kaya hindi siya mag stretch sa buong height ng window
#ang expand kasi dinidivide niya lahat kung ilan ang merong space sa window, at kapag expand=True siya ay magbibigay ng equal space sa lahat ng widgets na may expand=True, kaya kapag meron tayong dalawang frame na may expand=True ay magbibigay sila ng equal space sa window, kaya mapupunta sila sa gitna ng window

label = tk.Label(top_frame, text="This is a Frame!", bg="blue", fg="gray", font=("Arial", 24, 'bold'))
label.pack(expand=True) #also mag auto shrink siya kasi sa true yung expand

#top_frame.pack_propagate(False) 
#eto naman ay pwedeng gamitin para hindi mag shrink yung frame sa laki ng label, pero since nag lagay tayo ng specific width at height sa frame, hindi na natin kailangan gamitin ito kasi hindi na siya mag shrink sa laki ng label
#etong .pack_propagate(False) ay ginagamit para hindi mag shrink at gamitin natin yung dinictate naten na width at height ng frame sa top_frame
root.mainloop()
