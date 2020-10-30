from ..utils import tk, Alignment


class Text():

    __tk_object = None

    def __init__(self, text, width=None, height=None):
        self.text = text
        self.width = width
        self.height = height
        self.__tk_object = None

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_object = tk.Label(
                window, text=self.text, width=self.width, height=self.height)
        self.__tk_object.grid(
            row=row, column=column, sticky=Alignment.get_sticky_value_from_alignment(alignment))

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

class MultilineText():

    __tk_object = None

    def __init__(self, text, width=None, height=None):
        self.text = text
        self.width = width
        self.height = height
        self.__tk_object = None

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_object = tk.Message(window, text=self.text, width=self.width, height=self.height)
        self.__tk_object.grid(row=row, column=column, sticky=Alignment.get_sticky_value_from_alignment(alignment))

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
