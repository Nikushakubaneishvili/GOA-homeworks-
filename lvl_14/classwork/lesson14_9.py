#შექმენით while ციკლი რომლის გამოყენებითაც გაიგებთ 0დან 10ის 
#ცათვლით კენტ რიცხვებს და შემდეგ იპოვის ამ კენტი რიცხვების ჯამს
total_odd_sum = 0 
number = 0 
while number <= 10: 
    if number % 2 != 0: 
        total_odd_sum += number
    number += 1
print(total_odd_sum) 
