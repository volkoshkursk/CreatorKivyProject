# -*- coding: utf-8 -*-
#
# This file created with KivyCreatorProject
# <https://github.com/HeaTTheatR/KivyCreatorProgect
#
# Copyright (c) 2019 Ivanov Yuri and KivyMD
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>
#
# LICENSE: MIT

from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.properties import ListProperty

from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.theming import ThemableBehavior
from kivymd.vendor.navigationdrawer import NavigationDrawer


Builder.load_string("""
#:import Window kivy.core.window.Window


<ModifiedNavigationDrawer>:
    canvas:
        Color:
            rgba: root.theme_cls.bg_light
        Rectangle:
            size: root.size
            pos: root.pos
    canvas.before:
        Color:
            rgba: root.shadow_color
        Rectangle:
            size: Window.size
            pos: 0, 0

    BoxLayout:
        size_hint_y: None
        orientation: 'vertical'
        height: self.minimum_height
""")


class ModifiedNavigationDrawer(BoxLayout, ThemableBehavior,
                               RectangularElevationBehavior):
    orientation = 'vertical'
    shadow_color = ListProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super(ModifiedNavigationDrawer, self).__init__(**kwargs)
