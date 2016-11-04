#!/usr/bin/env python

import signal

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

from indicator_plot.resources import ICON_PATH
from indicator_plot.textbox import PlotWindow

APP_NAME = 'indicator-plot'


class PlotIndicator(object):

    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            APP_NAME,
            ICON_PATH,
            AppIndicator3.IndicatorCategory.OTHER
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())

    def build_menu(self):
        menu = Gtk.Menu()
        plot = Gtk.MenuItem('Plot')
        plot.connect('activate', self.dialog)
        menu.append(plot)

        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def dialog(self, item):
        win = PlotWindow()
        win.move(800, 400)
        # win.connect('delete-event', Gtk.main_quit)
        win.show_all()

    def stop(self, source):
        Gtk.main_quit()


def main():
    PlotIndicator()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


if __name__ == "__main__":
    main()
