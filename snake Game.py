import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game with Levels")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off screen updates

# Snake setup
snake = []
for i in range(3):
    segment = turtle.Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(-20 * i, 0)
    snake.append(segment)

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score and Level setup
score = 0
level = 1
delay = 0.1

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score} | Level: {level}", align="center", font=("Courier", 16, "normal"))

# Controls
def go_up():
    if snake[0].heading() != 270:  # Prevent reverse
        snake[0].setheading(90)

def go_down():
    if snake[0].heading() != 90:
        snake[0].setheading(270)

def go_left():
    if snake[0].heading() != 0:
        snake[0].setheading(180)

def go_right():
    if snake[0].heading() != 180:
        snake[0].setheading(0)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Game loop
while True:
    screen.update()

    # Move the snake
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    snake[0].forward(20)

    # Check for collision with food
    if snake[0].distance(food) < 15:
        # Move food to random position
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        snake.append(new_segment)

        # Update score and level
        score += 10
        if score % 50 == 0:  # Increase level every 50 points
            level += 1
            delay -= 0.01  # Increase speed

        score_display.clear()
        score_display.write(f"Score: {score} | Level: {level}", align="center", font=("Courier", 16, "normal"))

    # Check for collision with wall
    if abs(snake[0].xcor()) > 290 or abs(snake[0].ycor()) > 290:
        score_display.clear()
        score_display.write("Game Over!", align="center", font=("Courier", 24, "normal"))
        break

    # Check for collision with itself
    for segment in snake[1:]:
        if snake[0].distance(segment) < 10:
            score_display.clear()
            score_display.write("Game Over!", align="center", font=("Courier", 24, "normal"))
            break

    # Delay between movements
    time.sleep(delay)

screen.mainloop()
