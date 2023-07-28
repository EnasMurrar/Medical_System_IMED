import tkinter as tk
from tkinter import ttk


def toggle_frame(hidden_frame, button):
    if hidden_frame.winfo_ismapped():
        hidden_frame.grid_forget()
        button.config(text="+")
    else:
        hidden_frame.grid(row=1, column=0, sticky="nsew")
        button.config(text="-")


def submit():
    print("Entry:", entry.get())


root = tk.Tk()
root.geometry("1535x800+0+0")

# Create a scrollbar widget
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.grid(row=0, column=1, sticky="ns")

# Create a canvas widget
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.grid(row=0, column=0, sticky="nsew")

# Configure the scrollbar to work with the canvas
scrollbar.config(command=canvas.yview)

# Create a frame inside the canvas
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)

# Configure the canvas to resize with the frame
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Add support for scrolling using laptop touchpad
canvas.bind("<Enter>", lambda event: canvas.focus_set())
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * int(event.delta / 120), "units"))

frame1 = tk.Frame(scrollable_frame)
frame1.grid(row=0, column=0, sticky="nsew")

# Create the first plus button
button1 = tk.Button(frame1, text="+", width=20, height=10, command=lambda: toggle_frame(hidden_frame1, button1))
button1.grid(row=0, column=0)

# Create the first hidden frame
hidden_frame1 = tk.Frame(scrollable_frame, bg="blue", height=100)
hidden_frame1.grid(row=1, column=0, sticky="nsew")
hidden_frame1.grid_forget()

# Add widgets to the first hidden frame
tk.Label(hidden_frame1, text="Frame 1", height=50).pack()

frame2 = tk.Frame(scrollable_frame)
frame2.grid(row=1, column=0, sticky="nsew")

# Create the second plus button
button2 = tk.Button(frame2, text="+", width=20, height=10, command=lambda: toggle_frame(hidden_frame2, button2))
button2.grid(row=0, column=0)

# Create the second hidden frame
hidden_frame2 = tk.Frame(scrollable_frame, height=1000, bg="red")
hidden_frame2.grid(row=2, column=0, sticky="nsew")
hidden_frame2.grid_forget()

# Add widgets to the second hidden frame
tk.Label(hidden_frame2, text="Frame 2", height=30).pack()
entry = tk.Entry(hidden_frame2)
entry.pack()
button = tk.Button(hidden_frame2, text="Submit", command=submit)
button.pack()

frame3 = tk.Frame(scrollable_frame)
frame3.grid(row=2, column=0, sticky="nsew")

# Create the third plus button
button3 = tk.Button(frame3, text="+", width=20, height=10, command=lambda: toggle_frame(hidden_frame3, button3))
button3.grid(row=0, column=0)

# Create the third hidden frame
hidden_frame3 = tk.Frame(scrollable_frame, height=1000, bg="black")
hidden_frame3.grid(row=3, column=0, sticky="nsew")
hidden_frame3.grid_forget()

# Add widgets to the third hidden frame
tk.Label(hidden_frame3, text="Frame 3", height=30).pack()
entry = tk.Entry(hidden_frame3)
entry.pack()
button = tk.Button(hidden_frame3, text="Submit", command=submit)
button.pack()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
