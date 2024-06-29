#მომხმარებელს შემოატანინეთ ორი რიცხვი. ამის შემდეგ კი
#for loop ის მეშვეობით იპოვეთ ყველა რიცხვი ამ ორ რიცხვს შორის,
#შემდეგ გამოთვალეთ ამ რიცხვების ჯამი და საბოლოოდ კი დაპრინტეთ ტერმინალში
summ_numbers=0
num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))
for i in range(num1, num2) : 
    summ_numbers += i 
print(summ_numbers) 