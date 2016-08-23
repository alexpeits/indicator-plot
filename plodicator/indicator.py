#!/usr/bin/env python

# This code is an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html

import os
import signal
import webbrowser

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

from textbox import PlotWindow


APP_NAME = 'plot-indicator'
ICON = 'bar_chart_alt.svg'
# ICON = 'graph.svg'
HERE = os.path.abspath(os.path.dirname(__file__))
ICON_PATH = os.path.join(HERE, 'icons', ICON)
BROWSERS = webbrowser._browsers.keys()


class PlotIndicator:

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
