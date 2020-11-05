from ..utils import tk, Alignment


class Text():

    __tk_object = None

    def __init__(self, text, width=None, height=None, hidden=False):
        self.text = text
        self.width = width
        self.height = height
        self.initially_hidden = hidden
        self.hidden_status = True

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_object = tk.Label(
                window, text=self.text, width=self.width, height=self.height)
        self.row = row
        self.column = column
        self.sticky = Alignment.get_sticky_value_from_alignment(alignment)
        if not self.initially_hidden:
            self.show()

    def get_text(self):
        return self.text
    
    def set_text(self, text):
        self.text = text
        if self.__tk_object:
            self.__tk_object['text'] = self.text

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
