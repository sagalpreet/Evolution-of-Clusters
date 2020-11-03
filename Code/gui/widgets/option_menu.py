from ..utils import tk, Alignment


class OptionMenu():

    __tk_object = None
    __tk_variable = None

    def __init__(self, values, selected_index=0, callback=None):
        assert len(values) > 0, "Provide at least one value for OptionsMenu"
        assert len(values) > selected_index >= 0, "Selected index out of bounds"
        self.values = values
        self.selected_index = selected_index
        self.callback = callback
        self.hidden_status = True

    def __make_callback(self):
        if self.callback:
            self.callback(*self.get_value())

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_variable = tk.StringVar(
                value=self.values[self.selected_index])
            self.__tk_object = tk.OptionMenu(
                window, self.__tk_variable, *self.values, command=lambda x: self.__make_callback())
        self.row = row
        self.column = column
        self.sticky = Alignment.get_sticky_value_from_alignment(alignment)
        self.show()

    def get_value(self):
        if(self.__tk_variable):
            selected_value = self.__tk_variable.get()
            selected_index = -1
            for i in range(0, len(self.values)):
                if(self.values[i] == selected_value):
                    selected_index = i
                    break
            return (selected_index, selected_value)
        else:
            return self.selected_index, self.values[self.selected_index]

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
