from ..utils import tk, Alignment


class CheckBox():

    __tk_object = None
    __tk_variable = None

    def __init__(self, text, selected=False, width=None, height=None, callback=None):
        self.text = text
        self.selected = selected
        self.width = width
        self.height = height
        self.hidden_status = True
        self.callback = callback

    def __make_callback(self):
        if self.callback:
            self.callback(self.get_value())

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_variable = tk.BooleanVar(value=self.selected)
            self.__tk_object = tk.Checkbutton(window, text=self.text, variable=self.__tk_variable,
                                              width=self.width, height=self.height, command=lambda: self.__make_callback())
        self.row = row
        self.column = column
        self.sticky = Alignment.get_sticky_value_from_alignment(alignment)
        self.show()

    def get_value(self):
        if(self.__tk_variable):
            return self.__tk_variable.get()
        else:
            return self.selected

    def is_hidden(self):
        return self.hidden_status

    def hide(self):
        if self.__tk_object:
            self.__tk_object.grid_forget()
        self.hidden_status = True

    def show(self):
        if self.__tk_object:
            self.__tk_object.grid(row=self.row, column=self.column, sticky=self.sticky)
            self.hidden_status = False

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
