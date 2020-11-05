from ..utils import tk, Alignment

class Grid():

    __tk_object = None

    def __init__(self, widgets, width=None, height=None, hidden=False, alignment=Alignment.Center):
        self.widgets = widgets
        self.width = width
        self.height = height
        self.alignment = alignment.Center
        self.grid_state = tk.NORMAL
        self.initially_hidden = hidden
        self.hidden_status = True

    def makeTkObject(self, window, row, column, alignment):
        if(not self.__tk_object):
            self.__tk_object = tk.Frame(
                window, width=self.width, height=self.height)
            for grid_y in range(len(self.widgets)):
                row_of_widgets = self.widgets[grid_y]
                if(row_of_widgets):
                    for grid_x in range(len(row_of_widgets)):
                        widget = row_of_widgets[grid_x]
                        if(widget):
                            widget.makeTkObject(
                                self.__tk_object, row=grid_y, column=grid_x, alignment=alignment)
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
        return self.grid_state == tk.DISABLED

    def is_enabled(self):
        return not self.is_disabled()

    def disable(self):
        if(self.__tk_object):
            self.grid_state = tk.DISABLED
            for row_of_widgets in self.widgets:
                for widget in row_of_widgets:
                    if widget:
                        widget.disable()

    def enable(self):
        if(self.__tk_object):
            self.grid_state = tk.NORMAL
            for row_of_widgets in self.widgets:
                for widget in row_of_widgets:
                    if widget:
                        widget.enable()

