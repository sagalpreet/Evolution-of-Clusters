from .utils import tk, Alignment

from .widgets.button import Button
from .widgets.check_box import CheckBox
from .widgets.grid import Grid
from .widgets.option_menu import OptionMenu
from .widgets.slider import Slider
from .widgets.spacing import Spacing
from .widgets.text import Text, MultilineText


def create_gui(widgets, title='Evolution of Clusters', alignment=Alignment.Center):
    """
    Creates a window from a 2D array of widgets

    This will block further execution until the window is open
    """
    main_window = tk.Tk()
    main_window.wm_title(title)
    for grid_y in range(len(widgets)):
        row_of_widgets = widgets[grid_y]
        if(row_of_widgets):
            for grid_x in range(len(row_of_widgets)):
                widget = row_of_widgets[grid_x]
                if(widget):
                    widget.makeTkObject(
                        main_window, row=grid_y, column=grid_x, alignment=alignment)
    main_window.mainloop()
