import pyxel
import math

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
BALL_SIZE = 2
BALL_SPEED = 2

class Vec2:     #This method converts the given x and y value and converts
    def __init__(self, x, y):       #it into an easy to access vector.
        self.x = x
        self. y = y

class Vec2_norm:
    def __init__(self, x, y):
        self.magnitude = math.sqrt(x * x + y * y)
        self.x = x / self.magnitude * BALL_SPEED
        self.y = y / self.magnitude * BALL_SPEED

class Ball:
    def __init__(self, px, py, vx, vy):
        self.position = Vec2(px, py)
        self.velocity = Vec2_norm(vx, vy)
    def update(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        if self.position.y >= SCREEN_HEIGHT - BALL_SIZE:
            self.velocity.y = -self.velocity.y
        if self.position.y <= BALL_SIZE:
            self.velocity.y = -self.velocity.y
   
        #if self.position.x >= SCREEN_WIDTH - BALL_SIZE:
            #self.velocity.x = -self.velocity.x
        #if self.position.x <= BALL_SIZE:
            #self.velocity.x = -self.velocity.x

class Pong:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_WIDTH)
        self.ball = Ball(20, 20, 2, 2)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.ball.update()

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    
    def draw(self):
        pyxel.cls(3)
        pyxel.circ(
            self.ball.position.x,
            self.ball.position.y,
            BALL_SIZE,
            0
        )



Pong()




