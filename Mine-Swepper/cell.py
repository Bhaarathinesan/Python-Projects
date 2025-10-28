import sys
from tkinter import Button,Label
import random
import settings
import ctypes
import sys

class cell:
    all=[]
    cell_count=settings.CELL_COUNT
    cell_count_label_object=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.is_opened=False
        self.is_mine_candidate=False
        self.cell_btn_object=None
        self.x=x
        self.y=y
        #append the object to the cell.all list
        cell.all.append(self)


    def create_btn_object(self,location):
        btn=Button(
            location,
            width=6,
            height=2
        )
        btn.bind('<Button-1>',self.left_click_actions)
        btn.bind('<Button-3>',self.right_click_actions)
        self.cell_btn_object=btn

    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells left:{cell.cell_count}",
            font=("",15)
        )
        cell.cell_count_label_object=lbl

    def left_click_actions(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
    #if remaining cell count is equal to mines count then the player won
            if cell.cell_count==settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over',0)
    #cancel all the event on left and right click if the cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self,x,y):
        #Return a cell object based on the value of x,y
        for Cell in cell.all:
            if Cell.x==x and Cell.y==y:
                return Cell
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        cells = [Cell for Cell in cells if Cell is not None]
        return cells
    @property
    def surrounded_cells_mines_length(self):
        counter=0
        for Cell  in self.surrounded_cells:
            if Cell.is_mine:
                counter+=1

        return counter

    def show_cell(self):
        if not self.is_opened:
            cell.cell_count-=1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            #Replace the text of cell count label with the newer count
            if cell.cell_count_label_object:
                cell.cell_count_label_object.configure(
                    text=f"Cells left:{cell.cell_count}"
                )
                #if this is a mine candidate , then for safety, we should configure
                #the background color to the SystemButtonFace
                self.cell_btn_object.configure(
                    bg='SystemButtonFace'
                )
        #Mark the cell as opened(use it as last line of the method)
        self.is_opened=True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game over', 0)
        sys.exit()

    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate=True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate=False

    @staticmethod

    def randomize_mines():
        picked_Cells=random.sample(
            cell.all, settings.MINES_COUNT
        )
        for picked_Cell in picked_Cells:
            picked_Cell.is_mine=True

    def __repr__(self):
        return f"cell({self.x},{self.y})"
