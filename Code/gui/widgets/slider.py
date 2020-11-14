from ..utils import tk, Alignment
from .widget import Widget


class Slider(Widget):

    tk_object: tk.Scale = None
    tk_variable: tk.DoubleVar = None

    def __init__(self, min_value, max_value, default_value=None, fractional=False, thickness=None, length=None, hidden=False, callback=None):
        super().__init__(hidden=hidden)
        self.min_value = min_value
        self.max_value = max_value
        self.fractional = fractional
        self.tick_interval = (max_value - min_value) / \
            ((length if length else 100)/100)
        self.default_value = default_value if (default_value) else min_value
        self.thickness = thickness
        self.length = length
        self.callback = callback

    def __make_callback(self):
        if(self.callback):
            self.callback(self.tk_variable.get())

    def _initialize_tk_object(self, window):
        self.tk_variable = tk.DoubleVar(value=self.default_value)
        self.tk_object = tk.Scale(window, from_=self.min_value, to=self.max_value, resolution=0.0 if self.fractional else 1, tickinterval=self.tick_interval, variable=self.tk_variable,
                                    width=self.thickness, length=self.length, orient=tk.HORIZONTAL, command=lambda _: self.__make_callback())

    def get_value(self):
        if(self.tk_variable):
            return self.tk_variable.get()
        else:
            return self.default_value
