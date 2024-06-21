from turtle import * 

#draw a rectangle 
color("navy blue")
 
begin_fill()


penup()
goto(-330,-330)    
pendown()  


speed(100) 
width(7) 

forward(800)
left(90) 


forward(300) 
left(90)  
 
 
forward(800) 
left(90)  
 
forward (300)  
left(90)   

end_fill()

#end of rectangle 

forward(280) 
color("brown") 
begin_fill()
left(90)
forward(150) #height of the door 
right(90)
forward(200)
right(90)
forward(150)  
end_fill()   

 
penup()
goto(100, 100) 
pendown() 

color("maroon") 
begin_fill()

penup()
goto(-200, 150)
pendown() 
 
forward(180) 
right(90)  

forward(130)
right(90)

forward(180)
right(90) 

forward(130) 
right(90) 
 

penup()
goto(100, 100) 
pendown() 

penup()
goto(340, 150)
pendown() 

forward(180) 
left(90)  

forward(130)
left(90)

forward(180)
left(90) 

forward(130) 
left(90)  
 

penup()
goto(100, 100) 
pendown() 

penup()
goto(10, 150) 
pendown() 

forward(180) 
left(90)  

forward(130)
left(90)

forward(180)
left(90) 

forward(130) 
left(90)

end_fill() 

#end of castle 

color('blue')
begin_fill()


penup()
goto(-200, 150) 
pendown() 

right(150)
forward(130)
left(120)
forward(130)


penup()
goto(10, 150) 
pendown() 

left(180)
forward(130)
right(120)
forward(130)

penup()
goto(340,150) 
pendown() 

left(120)
forward(130)
right(120)
forward(130)

end_fill()





penup()
goto(340,100)
pendown() 


color("black") 
begin_fill()


left(150)
forward(150)

left(90)
forward(150) 

right(-90) 
forward(90) 

left(90) 
forward(150) 

end_fill() #end of flag

penup()
goto(220,230)
pendown()


color("green") 

right(180)  
circle(20,180) 
forward(10)
right(-90) 
forward(20)  
right(-90) 
forward(10)

penup()
goto(285,230)
pendown()


left(90) 
forward(40) 
right(90) 
forward(40) 
right(90) 
forward(40) 
right(90) 
forward(40)
backward(40) 
 

penup()
goto(330,190)
pendown()

pendown() 
left(110)
forward(45)
left(140)
forward(45)
left(180) 
forward(20) 
right(70) 
forward(18) 

penup()
goto(-620,-120)
pendown()

circle(30)
right(90)
forward(100)
right(90)
forward(50)
backward(100)
forward(50)
left(90)
forward(50)
backward(100)
forward(120) 

penup()
goto(-585,-380) 
pendown() 
left(200) 
forward(100) 
right(230) 
forward(100)

 
penup()
goto(-480,-280)
pendown()

color("purple") 
begin_fill()


setheading(60) 
forward(100)
setheading(-60) 
forward(100) 
setheading(180)
forward(100)

end_fill()

penup()
goto(-430,-190)
pendown()

setheading(5)
circle(25)

penup()
goto(-450,-280)
pendown()


left(-95)
forward(100)


penup()
goto(-415,-280)
pendown()


left(-1)
forward(100)


penup()
goto(-405,-230)
pendown() 

left(90)
forward(30)

penup()
goto(-455,-230)
pendown()

left(180)
forward(30) 


color("orange")
width(5)

penup()
goto(-595,-55)
pendown()

begin_fill()

forward(55)
left(280)
forward(40) 
left(210)
forward(30)
left(130) 
forward(55)
left(210)
forward(55)
left(120)
forward(30)
left(215)
forward(40) 

end_fill()


penup()
goto(-410,-135)
pendown()
 
begin_fill()

left(275)
forward(50) 
left(285) 
forward(40) 
left(220)
forward(30)
left(120)
forward(40)
left(210)
forward(40)
left(120) 
forward(30)
left(215) 
forward(46) 

end_fill()

exitonclick() 