from ..utils import tk, Alignment

class Spacing():

    __tk_object = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__tk_object = None

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_object = tk.Canvas(width=self.width, height=self.height)
        self.__tk_object.grid(row=row, column=column, sticky=Alignment.get_sticky_value_from_alignment(alignment))
