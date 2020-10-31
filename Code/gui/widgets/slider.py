from ..utils import tk, Alignment

class Slider():

    __tk_object: tk.Scale = None
    __tk_variable: tk.DoubleVar = None

    def __init__(self, min_value, max_value, default_value=None, fractional=False, thickness=None, length=None, callback=None):
        self.min_value = min_value
        self.max_value = max_value
        self.fractional = fractional
        self.tick_interval = (max_value - min_value)/((length if length else 100)/100)
        self.default_value = default_value if (default_value) else min_value
        self.thickness = thickness
        self.length = length
        self.callback = callback
        self.__tk_object = None

    def __make_callback(self):
        if(self.callback):
            self.callback(self.__tk_variable.get())

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_variable = tk.DoubleVar(value=self.default_value)
            self.__tk_object = tk.Scale(window, from_=self.min_value, to=self.max_value, resolution=0.0 if self.fractional else 1, tickinterval=self.tick_interval, variable=self.__tk_variable,
                                        width=self.thickness, length=self.length, orient=tk.HORIZONTAL, command=lambda _: self.__make_callback())
        self.__tk_object.grid(row=row, column=column, sticky=Alignment.get_sticky_value_from_alignment(alignment))

    def get_value(self):
        if(self.__tk_variable):
            return self.__tk_variable.get()
        else:
            return self.default_value

    def is_disabled(self):
        return self.__tk_object['state'] == tk.DISABLED

    def is_enabled(self):
        return not self.is_disabled()

    def disable(self):
        if(self.__tk_object):
            self.__tk_object['state'] = tk.DISABLED

    def enable(self):
        if(self.__tk_object):
            self.__tk_object['state'] = tk.NORMAL