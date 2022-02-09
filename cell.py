from tkinter import Button
import random
import settings

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append all objects in Cell.all list
        Cell.all.append(self)
        
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f'{self.x}, {self.y}'
        )
        # left click
        btn.bind('<Button-1>', self.left_click_actions) # event trigger, DON"T call the method, just pass it as a reference
        # right click
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn
    
    def left_click_actions(self, event):
        print(event)
        print('I am left clicked')
        
    def right_click_actions(self, event):
        print(event)
        print('I am right clicked')
        
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine= True
    
    def __repr__(self):
        return f'Cell({self.x}, {self.y})'