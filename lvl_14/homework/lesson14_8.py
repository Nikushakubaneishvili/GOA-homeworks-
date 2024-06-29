#Write a while loop that asks the user to guess a number
#between 1 and 10 until they get it right. The correct number is 7.
secret_number=7 
num=int(input("guess number 0 to 10:"))  
while num !=7:
    print("try again") 
    num=int(input("please re-enter number: "))  
print("congrats") 

