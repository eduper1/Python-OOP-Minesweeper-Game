from tkinter import *
import settings
import Utils

root = Tk()

# Over ride the settings of the windows
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

# create game frame
top_frame = Frame(
    root,
    bg='red', # Change later to black
    width=settings.WIDTH,
    height= Utils.height_prct(25)
)
top_frame.place(x=0, y=0)
left_frame = Frame(
    root,
    bg='yellow', # Change  latter to black
    width=Utils.width_prct(25),
    height=Utils.height_prct(75)
)
left_frame.place(x=0, y=Utils.height_prct(25))

# Run the window
root.mainloop()