import turtle
import random

score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-50, 400)
score_display.write(f'{score}', font=('Arial', 30, 'bold'))

def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write(f'{score}', font=('Arial', 30, 'bold'))

timer = 60

timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(400, 400)
timer_display.write(f'Time remaining: {timer}', font=('Arial', 15, 'bold'))

def update_timer():
    global timer
    if timer > 0:
        timer -= 1
        timer_display.clear()
        timer_display.write(f'Time remaining: {timer}', font=('Arial', 15, 'bold'))
        window.ontimer(update_timer, 1000)
    else:
        timer_display.clear()
        timer_display.goto(0, 0)
        timer_display.write('GaME oVER!', font=('Arial', 30, 'bold'))
        window.bye()

turtl = turtle.Turtle()
turtl.shape('turtle')
turtl.color('green')
turtl.shapesize(1)
turtl.speed(0)

apple = turtle.Turtle()
apple.shape('circle')
apple.color('red')
apple.speed(-1)

window = turtle.Screen()
window.title('Snake is crawling')
window.bgcolor('gray')
window.setup(startx=None, starty=None)

def move_right():
    turtl.forward(10)
    check_apple()
    check_pos()

def move_left():
    turtl.backward(10)
    check_apple()
    check_pos()

def move_up():
    turtl.left(15)
    check_apple()
    check_pos()

def move_down():
    turtl.right(15)
    check_apple()
    check_pos()

def clear():
    turtl.clear()

def home():
    turtl.penup()
    turtl.home()
    turtl.pendown()

def create_apple():
    apple.up()
    x = random.randint(-600, 600)
    y = random.randint(-400, 400)
    apple.goto(x, y)
    apple.down()

def check_apple():
    if turtl.distance(apple) < 10:
        create_apple()
        update_score()

def check_pos():
    if turtl.ycor() > 320:
        window.bye()

wall = turtle.Turtle()
wall.penup()
wall.speed('fastest')
wall.shape('square')
wall.shapesize(stretch_wid=1, stretch_len=100)
wall.goto(0, 350)

window.listen()
check_apple()
create_apple()
update_timer()
window.onkeypress(move_right, 'w')
window.onkeypress(move_left, 's')
window.onkeypress(move_up, 'd')
window.onkeypress(move_down, 'a')
window.onkeypress(clear, 'c')
window.onkeypress(home, 'h')

window.mainloop()