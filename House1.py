import turtle
turtle.tracer(2)
wn=turtle.Screen()
wn.setup(800,800)
wn.bgcolor('gold')

image=['image0.gif','image1.gif','image2.gif','image3.gif',\
       'image4.gif','image5.gif','image6.gif',\
       'image7.gif','image8.gif','image9.gif','image10.gif',\
       'image11.gif']

t=[]
for n in range(12):
    wn.addshape(image[n])
    t.append(turtle.Turtle())
    t[n].up()
    t[n].shape(image[n])


def drag_handler(turtle, x, y):
    #turtle.ondrag(None)  # disable ondrag event inside drag_handler
    turtle.goto(x, y)
    #turtle.ondrag(turtle,drag_handler(turtle, x, y))
    #turtle.ondrag(lambda x, y, turtle=turtle: drag_handler(turtle, x, y))


t[0].ondrag(lambda x, y: drag_handler(t[0], x, y))
t[1].ondrag(lambda x, y: drag_handler(t[1], x, y))
t[2].ondrag(lambda x, y: drag_handler(t[2], x, y))
t[3].ondrag(lambda x, y: drag_handler(t[3], x, y))
t[4].ondrag(lambda x, y: drag_handler(t[4], x, y))
t[5].ondrag(lambda x, y: drag_handler(t[5], x, y))
t[6].ondrag(lambda x, y: drag_handler(t[6], x, y))
t[7].ondrag(lambda x, y: drag_handler(t[7], x, y))
t[8].ondrag(lambda x, y: drag_handler(t[8], x, y))
t[9].ondrag(lambda x, y: drag_handler(t[9], x, y))
t[10].ondrag(lambda x, y: drag_handler(t[10], x, y))
t[11].ondrag(lambda x, y: drag_handler(t[11], x, y))


