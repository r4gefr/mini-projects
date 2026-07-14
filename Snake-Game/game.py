from tkinter import *
import random

# ---- Config ----
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
START_SPEED = 100
MIN_SPEED = 40
SPEED_STEP = 3 


class Snake:
    def __init__(self):
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = [
            canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                     fill=SNAKE_COLOR, tag="snake")
            for x, y in self.coordinates
        ]


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                            fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    global speed
    if paused:
        window.after(100, next_turn, snake, food)
        return

    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    x %= GAME_WIDTH
    y %= GAME_HEIGHT

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score:{score}")
        canvas.delete("food")
        food = Food()
        speed = max(MIN_SPEED, speed - SPEED_STEP)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(speed, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    opposite = {'left': 'right', 'right': 'left', 'up': 'down', 'down': 'up'}
    if direction != opposite.get(new_direction):
        direction = new_direction


def toggle_pause(event=None):
    global paused
    paused = not paused
    label.config(text=f"Score:{score}" + ("  [PAUSED]" if paused else ""))


def check_collisions(snake):
    x, y = snake.coordinates[0]
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 - 40,
                        font=('consolas', 60), text="GAME OVER", fill="red")
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 30,
                        font=('consolas', 25), text=f"Score: {score}  (press R to restart)",
                        fill="white")


def restart(event=None):
    global snake, food, score, direction, speed, paused
    canvas.delete(ALL)
    score = 0
    direction = 'down'
    speed = START_SPEED
    paused = False
    label.config(text=f"Score:{score}")
    snake = Snake()
    food = Food()
    next_turn(snake, food)


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'
speed = START_SPEED
paused = False

label = Label(window, text=f"Score:{score}", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
x = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
y = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+{x}+{y}")

window.bind('<Left>', lambda e: change_direction('left'))
window.bind('<Right>', lambda e: change_direction('right'))
window.bind('<Up>', lambda e: change_direction('up'))
window.bind('<Down>', lambda e: change_direction('down'))
window.bind('<space>', toggle_pause)
window.bind('r', restart)
window.bind('R', restart)

snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()