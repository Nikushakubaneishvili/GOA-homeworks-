from turtle import * 


#we want to paint a house 

#step 1: draw a square 
penup()
goto(-100,-100) 
pendown() 


speed(30) 
width(7) 
color("blue")  
begin_fill()
forward(200)
left(90) 

forward(200)
left(90) 

forward(200) 
left(90) 

forward (200) 
left(90) 
end_fill() 
#end of square 

#drawing a door 


forward(70) 
color("brown") 
begin_fill()
left(90)
forward(120) #height of the door 
right(90)
forward(60)
right(90)
forward(120) 
end_fill() 

penup()
goto(100, 100) 
pendown() 



color("red") 
begin_fill()
right(150)
forward(200)
left(120)
forward(200) 
end_fill() 

penup()
goto(-80, 80) 
pendown()
 


#draw a window1

penup()
goto(-80, 80)
pendown()
color("green") 
begin_fill()
left(30) 
forward(50)
left(90)  
forward(50)
left(90)
forward(50)
left(90)
forward(50)  
left(90) 
end_fill()  
#end of window1


penup()
goto(30, 80)  
pendown()
color("green") 
begin_fill()

forward(50)
left(90)  
forward(50)
left(90)
forward(50)
left(90)
forward(50)  
left(90) 
end_fill()  



exitonclick() 