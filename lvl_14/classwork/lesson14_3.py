#შექმენით for ციკლი რომლის გამოყენებითაც გაიგებთ ყველა 5ის ჯერად რიცხვს 0იდან 100ის
#ჩათვლით და შემდეგ გამოიტანთ ამ 5ის ჯერადი რიცხვების ჯამს
summ_multiples_of_5 = 0
for number in range(0, 101, 5) :  
    summ_multiples_of_5 += number 

print(summ_multiples_of_5)  