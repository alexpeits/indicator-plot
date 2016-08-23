import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk

from backend import plot


class PlotWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Plot")
        self.set_size_request(300, 70)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.func = Gtk.Entry()
        # self.entry.set_text("")
        self.func.connect('activate', self.on_activate)
        vbox.pack_start(self.func, True, True, 0)

        self.range = Gtk.Entry()
        self.range.set_text('0-100')
        self.range.connect('activate', self.on_activate)
        vbox.pack_start(self.range, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        self.btn = Gtk.Button.new_with_label('Plot')
        self.btn.connect('clicked', self.on_activate)
        hbox.pack_start(self.btn, True, True, 0)

    def on_activate(self, _):
        func = self.func.get_text()
        range_ = self.range.get_text().split('-')
        left, right = map(int, range_)
        plot(func, left, right)
        # self.emit('delete-event', Gdk.Event())
        self.destroy()


if __name__ == '__main__':
    win = PlotWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
