from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def inRange( pTarget, pMin, pMax ):
    ret = (pTarget >= pMin) and (pTarget <= pMax)
    return ret

def onClick( *args):
    col = args[0]
    row = args[1]

    # 波紋処理
    if( inRange(col-1, 0, 4) ):
        array[col-1][row].set(not array[col-1][row].get())

    for r in range(row - 1, row + 2):
        if( (r != row) and inRange(r, 0, 4) ):
            print(r)
            array[col][r].set(not array[col][r].get())

    if( inRange(col+1, 0, 4) ):
        array[col+1][row].set(not array[col+1][row].get())

    # クリア判定
    clear = True
    for c in range(5):
        for r in range(5):
            clear &= array[c][r].get()

    if( clear == True):
        messagebox.showinfo('おめでとう！','やるじゃない！')


root = Tk()
root.title("puzzle")

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid( column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

array = [[BooleanVar() for j in range(5)] for idx in range(5) ]

for column in range(5):
    for row in range(5):
        ttk.Checkbutton(mainframe, command=lambda c=column, r=row : onClick(c, r), variable=array[column][row]).grid(column=column, row=row, sticky=(N, W, E, S) )

root.bind('<Return>', onClick)
root.mainloop()
