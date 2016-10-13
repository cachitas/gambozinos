from kivy.app import App

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.vector import Vector


class CircularButton(ButtonBehavior, Widget):
    # radius = NumericProperty()

    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

    def on_press(self):
        print(self.color, self.size, self.center, self.width / 2)


class GambozinosGame(Widget):

    def update(self, dt):
        print("Updating", dt)


class GambozinoWidget(Widget):

    def on_touch_down(self, touch):
        print(touch)


class MainScreen(Screen):

    def start(self):
        self.manager.current = 'battle'


class BattleScreen(Screen):
    pass


class GambozinosApp(App):

    def build(self):
        w = BattleScreen()
        w.on_enter()
        return w


if __name__ == '__main__':
    GambozinosApp().run()
