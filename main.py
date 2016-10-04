from kivy.app import App

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen


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

    def on_enter(self):
        self.ids.cooldown_indicator.value = 0
        self.cd_refresh = Clock.schedule_interval(self.cooldown, 1.0/60.0)

    def on_leave(self):
        self.ids.cooldown_indicator.value = 0
        self.cd_refresh.cancel()

    def cooldown(self, dt):
        indicator = self.ids.cooldown_indicator
        if indicator.value < indicator.max:
            indicator.value += 1
        else:
            indicator.value = 0


class GambozinosApp(App):
    pass


if __name__ == '__main__':
    GambozinosApp().run()
