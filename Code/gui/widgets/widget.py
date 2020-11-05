from ..utils import tk, Alignment

class Widget():
    __tk_object = None

    def __init__(self, hidden=False):
        self.initially_hidden = hidden

    def getNewTkObject(self, window, row, column, alignment):
        raise Error('"getNewTkObject" function not implemented (contact Aman Palariya if you see this error)')

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_object = self.getNewTkObject(window, row, column, alignment)
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
