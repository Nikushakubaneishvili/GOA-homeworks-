from turtle import * 

#draw a rectangle 

penup()
goto(-330,-330)    
pendown()  


speed(30) 
width(7) 

forward(800)
left(90) 


forward(300) 
left(90)  
 
 
forward(800) 
left(90)  
 
forward (300)  
left(90)   
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

penup()
goto(-200, 150)
pendown() 

forward(180) 
left(90)  
 
exitonclick() 