#while loop-ის მეშვეობით მომხმარებელს იქამდე შემოატანინეთ
#სწორი პაროლი სანამ ეს პაროლი არ იქნება სწორი დაამატეთ 
#if რომ გამოიტანოტ იმის რაოდენობა თუ რამდენჯერ დაგჭირდათ პაროლის შეყვანა

correct_password = "nikusha2008"  # მაგალითისთვის სწორი პაროლი
entered_password = ""
attempts = 0

while entered_password != correct_password:
    if attempts > 0:
        print("error! try again")
    
    entered_password = input("password: ")
    attempts += 1

print("access granted, correct password.")
print (attempts)  
