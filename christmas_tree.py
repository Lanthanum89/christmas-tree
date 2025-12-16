import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("midnight blue")
screen.title("Sparkling Christmas Tree")
screen.setup(width=800, height=800)

tree = turtle.Turtle()
tree.speed(0)
tree.hideturtle()

def draw_trunk():
    tree.penup()
    tree.goto(-30, -300)
    tree.pendown()
    tree.color("saddle brown")
    tree.begin_fill()
    for _ in range(2):
        tree.forward(60)
        tree.left(90)
        tree.forward(80)
        tree.left(90)
    tree.end_fill()

def draw_tree():
    tree.penup()
    tree.goto(0, -220)
    tree.pendown()
    
    tree_colors = ["forest green", "dark green", "green"]
    sizes = [240, 180, 120]
    y_positions = [-220, -100, 40]
    
    for i in range(3):
        tree.penup()
        tree.goto(-sizes[i]//2, y_positions[i])
        tree.pendown()
        tree.color(tree_colors[i])
        tree.begin_fill()
        tree.goto(sizes[i]//2, y_positions[i])
        tree.goto(0, y_positions[i] + sizes[i]//1.5)
        tree.goto(-sizes[i]//2, y_positions[i])
        tree.end_fill()

def draw_star(x, y, size, color):
    tree.penup()
    tree.goto(x, y)
    tree.setheading(0)
    tree.color(color)
    tree.begin_fill()
    for _ in range(5):
        tree.forward(size)
        tree.right(144)
    tree.end_fill()

class Ornament:
    def __init__(self, x, y, size, colors):
        self.x = x
        self.y = y
        self.size = size
        self.colors = colors
        self.current_color = 0
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
    
    def draw(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.color(self.colors[self.current_color])
        self.turtle.begin_fill()
        self.turtle.circle(self.size)
        self.turtle.end_fill()
    
    def sparkle(self):
        self.current_color = (self.current_color + 1) % len(self.colors)
        self.draw()

draw_trunk()
draw_tree()
draw_star(0, 180, 30, "gold")

ornaments = []
ornament_positions = [
    (-80, -150), (80, -150), (-40, -150),
    (-60, -50), (60, -50), (0, -80),
    (-30, 20), (30, 20), (0, 50),
    (-15, 100), (15, 100)
]

colors_sets = [
    ["red", "dark red", "red"],
    ["blue", "dark blue", "blue"],
    ["gold", "yellow", "gold"],
    ["magenta", "purple", "magenta"],
    ["cyan", "turquoise", "cyan"]
]

for pos in ornament_positions:
    colors = random.choice(colors_sets)
    ornament = Ornament(pos[0], pos[1], random.randint(8, 12), colors)
    ornament.draw()
    ornaments.append(ornament)

class SparkleEffect:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle.color("white")
    
    def sparkle_at(self, x, y, size):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.setheading(0)
        for _ in range(4):
            self.turtle.forward(size)
            self.turtle.backward(size)
            self.turtle.right(90)

sparkle_effect = SparkleEffect()

def animate():
    for ornament in ornaments:
        if random.random() < 0.3:
            ornament.sparkle()
    
    sparkle_effect.turtle.clear()
    for _ in range(5):
        x = random.randint(-100, 100)
        y = random.randint(-200, 150)
        size = random.randint(5, 15)
        sparkle_effect.sparkle_at(x, y, size)
    
    if random.random() < 0.5:
        draw_star(0, 180, 30, random.choice(["gold", "yellow", "orange"]))
    
    screen.ontimer(animate, 500)

animate()
tree.penup()
tree.goto(0, -350)
tree.color("white")
tree.write("Click to close", align="center", font=("Arial", 12, "normal"))

screen.exitonclick()
