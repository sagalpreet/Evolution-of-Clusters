from ..utils import tk, Alignment

class ListBox():

    __tk_object = None

    def __init__(self, values, selected_index=0, width=None, height=None, hidden=False, callback=None):
        assert len(values)>0, "Provide at least one value for OptionsMenu"
        assert len(values)>selected_index>=0, "Selected index out of bounds"
        self.values = values
        self.selected_index = selected_index
        self.width = width
        self.height = height
        self.initially_hidden = hidden
        self.callback = callback

    def __make_callback(self):
        if self.callback:
            self.callback(*self.get_value())

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_object = tk.Listbox(window, width= self.width, height=self.height)
            for i in range(len(self.values)):
                self.__tk_object.insert(i+1, self.values[i])
            self.__tk_object.select_set(self.selected_index)
        self.row = row
        self.column = column
        self.sticky = Alignment.get_sticky_value_from_alignment(alignment)
        if not self.initially_hidden:
            self.show()

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

    def get_value(self):
        if(self.__tk_object):
            selected_index = self.__tk_object.curselection()[0]
            selected_value = self.values[selected_index]
            return selected_index, selected_value
        else:
            return self.selected_index, self.values[selected_value]

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
