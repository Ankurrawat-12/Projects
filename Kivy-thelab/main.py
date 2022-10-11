from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


# from random import randint


class WidgetsExamples(GridLayout):
    my_text = StringProperty("Hello!")
    text_input_str = StringProperty("Ankur")
    # slider_value_txt = StringProperty("0")
    count = 1
    on = BooleanProperty(False)

    def on_button_click(self):
        if self.on:
            self.my_text = str(self.count)
            self.count += 1

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.on = False
        else:
            widget.text = "ON"
            self.on = True

    def on_switch_active(self, widget):
        # print("widget : " + str(widget.active))
        pass

    def on_slider_value(self, widget):
        # print("Widget :- " + str(widget.value))
        # self.slider_value_txt = str(widget.value)
        pass

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "rl-tb"
        for i in range(0, 100):
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(text=str(i + 1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


"""    
        def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        """


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 100), width=2)
            Line(rectangle=(100, 50, 90, 100), width=5)
            self.rect = Rectangle(pos=(dp(300), dp(200)), size=(dp(80), dp(100)))

    def on_button_a_clicked(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff
        x += inc

        # self.rect.pos = (randint(0, 500), randint(0, 650))
        self.rect.pos = (x, y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1 / 60)

    def on_size(self, *args):
        # print("On size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)

    def update(self, dt):
        # print("Update")
        x, y = self.ball.pos
        self.check_collision()

    def check_collision(self):
        x, y = self.ball.pos
        if x + self.ball_size > self.width or x < 0:
            self.vx = - self.vx
            # x = self.width - self.ball_size
        if y + self.ball_size > self.height or y < 0:
            # y = self.height - self.ball_size
            self.vy = - self.vy
        self.ball.pos = (x + self.vx, y + self.vy)


class CanvasExample6(Widget):
    pass


class CanvasExample7(BoxLayout):
    pass


TheLabApp().run()
