#შექმენით while ციკლი რომლის გამოყენებითაც გაიგებთ ყველა 5ის ჯერად რიცხვს 0იდან 100ის 
#ჩათვლით და შემდეგ გამოიტანთ ამ 5ის ჯერადი რიცხვების ჯამს

number= 0
sum_multiples_of_5 = 0 
while number <= 100: 
    if number % 5 == 0 :
        sum_multiples_of_5 += number
    number += 1 
print(sum_multiples_of_5) 