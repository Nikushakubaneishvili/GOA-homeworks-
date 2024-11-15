name1="Nika"
name2="shaLva"
name3="RObo" 
 
print(name1.upper(), name2.upper(), name3.upper())   #ადიდებს ყველა ასობგერას სტრინგში
print(name1.lower(), name2.lower(), name3.lower())   #აპატარავებს ყველა ასობგერას სტრინგში
print(name1.capitalize(), name2.capitalize(), name3.capitalize())  #ადიდებს მხოლოდ პირველ ასობგერას სტრინგში 


cars=["mercedes", "bmw", "audi"] 
cars.append("opel")  #ამატებს ელემენტს სიის ბოლოში
cars.insert(1, "pagani")  #ამატებს ელემენტს კონკრეტულ ინდექსზე
cars.pop(3)  #აგდებს ელემენტს სიიდან
print(cars) 