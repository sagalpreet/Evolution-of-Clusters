from ..utils import tk, Alignment


class Button():

    __tk_object: tk.Button = None

    def __init__(self, text, width=None, height=None, callback=None):
        self.text = text
        self.width = width
        self.height = height
        self.callback = callback
        self.__tk_object: tk.Button = None

    def __make_callback(self):
        if(self.callback):
            self.callback()

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_object = tk.Button(
                window, text=self.text, width=self.width, height=self.height, command=self.__make_callback)
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
