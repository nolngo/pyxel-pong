import pyxel
import math

SCREEN_WIDTH = 244
SCREEN_HEIGHT = 120
BALL_SIZE = 2
BALL_SPEED = 2
PADDLE_SIZE = 6
BACKGROUND_COLOR = 3
ELEMENTS_COLOR = 0

class Vec2:     #This class converts the given x and y value and converts
    def __init__(self, x, y):       #it into an easy to access vector.
        self.x = x
        self.y = y

class Ball:
    def __init__(self, px, py, vx, vy):
        self.position = Vec2(px, py)
        self.velocity = Vec2(vx, vy)
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

class Paddle:
    def __init__(self, px, py):
        self.position = Vec2(px, py)
        self.velocity = 0
        self.hitBox = HitBox(
            self.position.x - PADDLE_SIZE / 4,
            self.position.y - PADDLE_SIZE,
            self.position.x + PADDLE_SIZE / 4,
            self.position.y + PADDLE_SIZE
        )

    def update(self):
        self.position.y += self.velocity
        self.hitBox = HitBox(
        self.position.x - PADDLE_SIZE / 4,
        self.position.y - PADDLE_SIZE,
        self.position.x + PADDLE_SIZE / 4,
        self.position.y + PADDLE_SIZE
        )

        if pyxel.btnp(pyxel.KEY_W):
            self.velocity = -2
        if pyxel.btnp(pyxel.KEY_S):
            self.velocity = 2
        if self.position.y - PADDLE_SIZE < 0:
            self.position.y = PADDLE_SIZE
            self.velocity = 0
        if self.position.y + PADDLE_SIZE > SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT - PADDLE_SIZE
            self.velocity = 0

        

class HitBox:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2



class PlayPong:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_WIDTH)
        self.ball = Ball(20, 20, 2, 2)
        self.paddles = [Paddle(10, 10), Paddle(SCREEN_WIDTH - 10, 10)]
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.ball.update()
        for paddle in self.paddles:
            paddle.update()
            if (paddle.hitBox.x1 < self.ball.position.x < paddle.hitBox.x2 and paddle.hitBox.y1 < self.ball.position.y < paddle.hitBox.y2): 
                self.ball.velocity.x = -self.ball.velocity.x
                self.score += 1
        if self.ball.position.x >= SCREEN_WIDTH - BALL_SIZE:
            pyxel.quit()
        if self.ball.position.x <= BALL_SIZE:
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(3)
        pyxel.circ(
            self.ball.position.x,
            self.ball.position.y,
            BALL_SIZE,
            ELEMENTS_COLOR
        )
        for paddle in self.paddles:
            pyxel.rect(
                paddle.hitBox.x1,
                paddle.hitBox.y1,
                paddle.hitBox.x2,
                paddle.hitBox.y2,
                ELEMENTS_COLOR
            )
        pyxel.text(
            SCREEN_WIDTH / 2,       #Makes the score appear in the middle of the X-axis
            SCREEN_HEIGHT / 12,     #Makes the score appear at the 1/12th top of the Y-axis
            str(self.score),
            ELEMENTS_COLOR
        )


PlayPong()