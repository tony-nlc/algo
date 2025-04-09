import turtle

t = turtle.Turtle()
t.speed(0) 

def draw_koch(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length //= 3
        draw_koch(length, depth - 1)
        t.left(60)
        draw_koch(length, depth - 1)
        t.right(120)
        draw_koch(length, depth - 1)
        t.left(60)
        draw_koch(length, depth - 1)

for _ in range(3):
    draw_koch(600, 5)  
    t.right(120)

turtle.done()
