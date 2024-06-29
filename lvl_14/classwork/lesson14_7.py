#while loop-ის მეშვეობით მომხმარებელს იქამდე შემოატანინეთ სწორი პაროლი სანამ ეს პაროლი არ იქნება სოწი
correct_password = "nikusha2008"
entered_password = "" 

while entered_password != correct_password:
    entered_password= input("please enter the correct password: ")
print("correct password entered. access granted!")  