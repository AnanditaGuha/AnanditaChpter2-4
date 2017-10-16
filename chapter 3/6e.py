import turtle
wn = turtle.Screen()
turt = turtle.Turtle()
si = int(input("how many sides"))
lo = int(input("how long should the sides be"))



for i in range(si):
    turt.forward(lo)
    turt.right(360/si)
      #return turt.pos()

