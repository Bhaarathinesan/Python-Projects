from tkinter import  *
import settings
import utils
from cell import cell

root=Tk()
#override the settings of the window
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)
top_frame=Frame(
    root,
    bg='black',#change the color to black later
    width=720,
    height=utils.height_prct(25)
)
top_frame.place(x=0,y=0)

game_title=Label(
    top_frame,
    bg='black',
    fg='white',
    text='Mine Sweeper',
    font=('',24)
)
game_title.place(
    x=utils.width_prct(25), y=0
)

left_frame=Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0,y=90)

centre_frame=Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
centre_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=cell(x, y)
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(
            column=x,row=y
        )
#call the label from the cell class
cell.create_cell_count_label(left_frame)
cell.cell_count_label_object.place(
    x=0,y=0
)
cell.randomize_mines()

#Run the window
root.mainloop()
