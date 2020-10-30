import tkinter as tk

from enum import Enum

class Alignment(Enum):
    TopLeft = 0
    TopCenter = 1
    TopRight = 2
    CenterLeft = 3
    Center = 4
    CenterRight = 5
    BottomLeft = 6
    BottomCenter = 7
    BottomRight = 8
    Stretch = 9

    @staticmethod
    def get_sticky_value_from_alignment(alignment):
        alignment = alignment.value
        if alignment==0:
            return tk.NW
        elif alignment==1:
            return tk.N
        elif alignment==2:
            return tk.NW
        elif alignment==3:
            return tk.W
        elif alignment==4:
            return None
        elif alignment==5:
            return tk.E
        elif alignment==6:
            return tk.SW
        elif alignment==7:
            return tk.S
        elif alignment==8:
            return tk.SE
        else:
            return tk.NSEW
