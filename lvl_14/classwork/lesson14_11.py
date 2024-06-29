#ექმენით while ციკლი რომლის გამოყენებითაც გაიგებთ ყველა 3ის ჯერად რიცხვს 0იდან 100ის ჩათვლით

number= 0
sum_multiples_of_3 = 0 
while number <= 100: 
    if number % 3 != 0 :
        sum_multiples_of_3 += number 
    number += 1 
print(sum_multiples_of_3) 