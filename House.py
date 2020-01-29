import turtle
turtle.tracer(3)
wn=turtle.Screen()
wn.setup(800,800)
wn.bgcolor('gold')

TEXT_FONT=('Arial', 20,'bold')
capture=turtle.Turtle()
capture.hideturtle() 
capture.up()
capture.setposition(-300,-300)
capture.write('Build a House dragging parts with a mouse', font=TEXT_FONT)


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
         
def dragging0(x, y):
    t[0].ondrag(None)
    t[0].goto(x, y)
    t[0].ondrag(dragging0)
    
def dragging1(x, y):
    t[1].ondrag(None)
    t[1].goto(x, y)
    t[1].ondrag(dragging1)
    
def dragging2(x, y):
    t[2].ondrag(None)
    t[2].goto(x, y)
    t[2].ondrag(dragging2)
    
def dragging3(x, y):
    t[3].ondrag(None)
    t[3].goto(x, y)
    t[3].ondrag(dragging3)
    
def dragging4(x, y):
    t[4].ondrag(None)
    t[4].goto(x, y)
    t[4].ondrag(dragging4)
    
def dragging5(x, y):
    t[5].ondrag(None)
    t[5].goto(x, y)
    t[5].ondrag(dragging5)
    
def dragging6(x, y):
    t[6].ondrag(None)
    t[6].goto(x, y)
    t[6].ondrag(dragging6)

def dragging7(x, y):
    t[7].ondrag(None)
    t[7].goto(x, y)
    t[7].ondrag(dragging7)

def dragging8(x, y):
    t[8].ondrag(None)
    t[8].goto(x, y)
    t[8].ondrag(dragging8)

def dragging9(x, y):
    t[9].ondrag(None)
    t[9].goto(x, y)
    t[9].ondrag(dragging9)

def dragging10(x, y):
    t[10].ondrag(None)
    t[10].goto(x, y)
    t[10].ondrag(dragging10)

def dragging11(x, y):
    t[11].ondrag(None)
    t[11].goto(x, y)
    t[11].ondrag(dragging11)

   
t[0].ondrag(dragging0)
t[1].ondrag(dragging1)
t[2].ondrag(dragging2)
t[3].ondrag(dragging3)
t[4].ondrag(dragging4)
t[5].ondrag(dragging5)
t[6].ondrag(dragging6)
t[7].ondrag(dragging7)
t[8].ondrag(dragging8)
t[9].ondrag(dragging9)
t[10].ondrag(dragging10)
t[11].ondrag(dragging11)

    
