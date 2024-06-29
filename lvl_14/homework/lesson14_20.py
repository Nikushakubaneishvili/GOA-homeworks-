#Calculate the sum of digits of a number entered by the user.
num=int(input("please enter number: "))
sum=0 
while num >0: 
    digit=num %10
    sum += digit
    num = num //10
print(sum)  