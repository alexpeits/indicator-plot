import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from indicator_plot.backend import plot
from indicator_plot.resources import ICON_PATH


class PlotWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Plot function')
        self.set_icon_from_file(ICON_PATH)
        self.set_size_request(300, 70)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.func = Gtk.Entry()
        # self.entry.set_text("")
        self.func.connect('activate', self.on_activate)
        vbox.pack_start(self.func, True, True, 0)

        rbox = Gtk.Box(spacing=6)
        vbox.pack_start(rbox, True, True, 0)

        range_label = Gtk.Label('Range:')
        rbox.pack_start(range_label, True, True, 0)

        self.left = Gtk.Entry()
        self.left.set_text('0')
        self.left.connect('activate', self.on_activate)
        rbox.pack_start(self.left, True, True, 0)

        dash = Gtk.Label('-')
        rbox.pack_start(dash, True, True, 0)

        self.right = Gtk.Entry()
        self.right.set_text('100')
        self.right.connect('activate', self.on_activate)
        rbox.pack_start(self.right, True, True, 0)

        bbox = Gtk.Box(spacing=6)
        vbox.pack_start(bbox, True, True, 0)

        self.btn = Gtk.Button.new_with_label('Plot')
        self.btn.connect('clicked', self.on_activate)
        bbox.pack_start(self.btn, True, True, 0)

    def on_activate(self, _):
        func = self.func.get_text()
        left = float(self.left.get_text())
        right = float(self.right.get_text())
        try:
            plot(func, left, right)
        except:
            pass
        self.destroy()


if __name__ == '__main__':
    win = PlotWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
