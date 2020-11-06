from ..utils import tk, Alignment
from .widget import Widget


class CheckBox(Widget):

    tk_object = None
    tk_variable = None

    def __init__(self, text, selected=False, width=None, height=None, hidden=False, callback=None):
        super().__init__(hidden=hidden)
        self.text = text
        self.selected = selected
        self.width = width
        self.height = height
        self.callback = callback

    def __make_callback(self):
        if self.callback:
            self.callback(self.get_value())

    def _initialize_tk_object(self, window):
        self.tk_variable = tk.BooleanVar(value=self.selected)
        self.tk_object = tk.Checkbutton(window, text=self.text, variable=self.tk_variable,
                                          width=self.width, height=self.height, command=lambda: self.__make_callback())

    def get_value(self):
        if(self.tk_variable):
            return self.tk_variable.get()
        else:
            return self.selected
