#Write a while loop that repeatedly asks the user to enter 
#a password until the correct password "password123" is entered.
password="password123" 
password2=input("type your password: ")
while password2 != password: 
 print("wrong password,try again: ")  
 password2=input("type your password again: ") 
print("correct password")  

