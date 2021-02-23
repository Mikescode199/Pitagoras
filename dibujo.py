import turtle as ttl

def Dibujar(a, b, h):

    screen = ttl.screensize(400)
    t = ttl.Turtle()
    t.forward(b)
    t.left(120)
    t.forward(h)
    t.left(120)
    t.forward(a)
    t.left(120)
    screen.done()






