#შექმენით while ციკლი რომლის გამოყენებითაც გაიგებთ 
#0დან 10ის ჩათვლით ლუწ რიცხვებს და შემდეგ იპოვის ამ ლუწი რიცხვების ჯამს

total_even_sum = 0 
number = 0 
while number <= 10: 
    if number % 2 == 0:
        total_even_sum += number
    number += 1
print(total_even_sum) 