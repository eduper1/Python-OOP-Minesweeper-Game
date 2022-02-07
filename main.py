from tkinter import *

root = Tk()

# Over ride the settings of the windows
root.configure(bg="black")
root.geometry('1020x720')
root.title("Minesweeper Game")
root.resizable(False, False)

# create game frame
top_frame = Frame(
    root,
    bg='red', # Change later to black
    width=1020,
    height=180
    
)

# Run the window
root.mainloop()