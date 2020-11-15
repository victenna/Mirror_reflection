import turtle,time
wn=turtle.Screen()
wn.setup(1000,750)
wn.bgpic('background.gif')
wn.addshape('source_Image.gif')
wn.addshape('receiver.gif')
wn.addshape('result.gif')
FONT=('Times New Roman',20,'bold')
FONT1=('Times New Roman',15,'bold')

XY=turtle.Turtle('arrow')             # axis X and Y
XY.fd(300)
XY.stamp()
XY.write('X ',font=FONT)
XY.up()
XY.goto(0,-200)
XY.setheading(90)
XY.down()
XY.fd(400)
XY.write('Y',font=FONT)

R=300
light=turtle.Turtle('arrow')       #source (light)
light.color('blue')
light.pensize(5)
light.up()
light.hideturtle()

Image=turtle.Turtle()            #Images with result angles alpha and betta 
Image.shape('result.gif')
Image.up()
Image.hideturtle()
Image.goto(-300,-100)
Image.showturtle()

Result=turtle.Turtle()
Result.up()
Result.hideturtle()

turtle.tracer(2)
alpha=int(wn.textinput('Угол падения луча на зеркало','alpha')) #Source angle

Result.goto(-350,250)
Result.write('Угол alpha=',font=FONT)
Result.goto(-200,250)
Result.write(alpha,font=FONT)
   
light.goto(0,0)
light.setheading(alpha)
light.fd(R)
light.setheading(180+alpha)
light.down()

Source1=turtle.Turtle('triangle')
Source1.shapesize(1,2)
Source1.color('blue')
Source1.up()
Source1.setheading(alpha)
Source1.fd(R)
Position=Source1.position()

Source_Image=turtle.Turtle()
Source_Image.shape('source_Image.gif')

Receiver=turtle.Turtle()
Receiver.shape('receiver.gif')
Receiver.up()
Receiver.goto(0,-300)

Mirror=turtle.Turtle('square')
Mirror.shapesize(0.5,10)
Mirror.color('red')

Mirror1=turtle.Turtle()
Mirror1.hideturtle()
Mirror1.color('red')
Mirror1.up()
Mirror1.goto(-70,30)
Mirror1.write('Mirror',font=FONT1)

turtle.tracer(3)
def mirror(angle):
    Mirror.setheading(angle)
    Mirror.goto(0,0)
    
A=True
k=0
while A:
    Source_Image.hideturtle()
    Source_Image.up()
    Source_Image.goto(0,0)
    Source_Image.setheading(alpha)
    Source_Image.fd(R+50)
    Source_Image.showturtle()
    Source_Image.stamp()
    light.showturtle()
    k=k+1
    betta=55+alpha/2-k*1
    mirror(betta)
    for j in range(50):
        light.fd(6)
        time.sleep(0.01)
    light.setheading(-180+2*betta-alpha)
               
    for i in range(50):
        light.fd(5)
        time.sleep(0.01)
        
    if betta!=45+alpha/2:
        time.sleep(1)
        Mirror.clear()
        light.clear()
    light.up()
    light.hideturtle()
    light.goto(0,0)
    light.setheading(alpha)
    light.fd(R)
    light.setheading(180+alpha)
    light.down()
    if betta==45+alpha/2:
        A=False
        Result.goto(100,-150)
        Result.write('Угол betta=',font=FONT)
        Result.goto(250,-150)
        Result.write(betta,font=FONT)
        




    
