import tkinter as tk

root = tk.Tk()          # Main window create
root.title("My App")    # Window ka title
root.geometry("400x300") # Window size
label = tk.Label(root, text="Welcome", bg="yellow", fg="red", font=("Arial", 14))
label.pack()
root.mainloop()         # Window run karne ke liye

