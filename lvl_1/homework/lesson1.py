name = "nika" 
#name არის ცვლადი 
# = არის ცვლადის მნიშვნელობის მიმნიჭებელი 


surname = "kubaneishvili"

# print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი 

name = "nika" 
age =16 # ეს არის int ( integer ) მთელი რიცხვი 
height = 173.5 #ეს არის float ტიპის ცვლადი (ათწილადი) 
#boolean (bool) ტიპის ცვლადი 

knows_programming = True #true ან false 
is_ugly = False #snakecase (უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False #ჯავასკრიპტული camelcase 


print(name + " " + surname)  

#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები 
#print(name + age ) 

print(type(age)) 
print(type(name)) 
print(type(surname)) 
print(type(height)) 
print(type(knows_programming)) 

print(name + " " + str(age))  

print(name + " " + str(age) + " " + surname + " " + str (height) + " " + str(knows_programming)) 