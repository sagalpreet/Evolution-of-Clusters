from ..utils import tk, Alignment
from .widget import Widget

class Grid(Widget):

    tk_object = None

    def __init__(self, widgets, width=None, height=None, hidden=False, alignment=Alignment.Center):
        super().__init__(hidden=hidden)
        self.widgets = widgets
        self.width = width
        self.height = height
        self.alignment = alignment.Center
        self.grid_state = tk.NORMAL
    
    def _initialize_tk_object(self, window, alignment):
        if(not self.tk_object):
            self.tk_object = tk.Frame(
                window, width=self.width, height=self.height)
            for grid_y in range(len(self.widgets)):
                row_of_widgets = self.widgets[grid_y]
                if(row_of_widgets):
                    for grid_x in range(len(row_of_widgets)):
                        widget = row_of_widgets[grid_x]
                        if(widget):
                            widget._make_tk_object(
                                self.tk_object, row=grid_y, column=grid_x, alignment=alignment)
    
    def _make_tk_object(self, window, row, column, alignment):
        if(not self.tk_object):
            self._initialize_tk_object(window, alignment)
        super()._initialize_grid_values(row, column, alignment)
        super()._show_hide_initially()


    def is_disabled(self):
        return self.grid_state == tk.DISABLED

    def is_enabled(self):
        return not self.is_disabled()

    def disable(self):
        if(self.tk_object):
            self.grid_state = tk.DISABLED
            for row_of_widgets in self.widgets:
                for widget in row_of_widgets:
                    if widget:
                        widget.disable()

    def enable(self):
        if(self.tk_object):
            self.grid_state = tk.NORMAL
            for row_of_widgets in self.widgets:
                for widget in row_of_widgets:
                    if widget:
                        widget.enable()

