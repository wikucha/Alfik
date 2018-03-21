from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import builder


def load_lang(file_name):
    lang = {}
    exec(open(file_name, encoding="utf-8").read(), lang)
    return lang

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update_ball(self, pilka):
        pilka.move()

        # bounce of paddles
        self.player1.bounce_ball(pilka)
        self.player2.bounce_ball(pilka)

        # bounce ball off bottom or top
        if (pilka.y < self.y) or (pilka.top > self.top):
            pilka.velocity_y *= -1

        # went of to a side to score point?
        if pilka.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if pilka.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def update(self, dt):

        self.update_ball(self.ball)
        self.update_ball(self.ball2)



    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        #lang=load_lang("lang/rus/config.py")
        layout = builder.Builder.load_file("pong.kv")
        #slowo = layout.ids.slowo
        #slowo.text = lang["translate"][litera]["word"]

        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()