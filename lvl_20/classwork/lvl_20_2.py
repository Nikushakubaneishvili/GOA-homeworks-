#უნდა შექმნათ ფუნქცია რომელსაც გადაეცემა სამი პარამეტრი 
#აქედან ორი იქნება რიცხვი ხოლო ერთი ოპერატორი 
#(ოპერატორი = string) და შეასრულეთ მასზე ოპერაციები 
def add(num1, num2, operation):
    # ამ ფუნქციით შექმნილია კალკულატორის ფუნქცია, რომელიც ასრულებს გამოსახულებას
    # num1 და num2 რიცხვებია, ხოლო operation არის სტრიქონი, რომელიც განსაზღვრავს მოქმედებას (+, -, *, /)
    if operation == "+":
        print(num1 + num2)  # დამატება
    elif operation == "-":
        print(num1 - num2)  # გამოკლება
    elif operation == "*":
        print(num1 * num2)  # გამრავლება
    elif operation == "/":
        print(num1 / num2)  # გაყოფა
    else:
        print("Invalid Operation")  # არასწორი ოპერაცია

add(9, 3, "+")   # გამოიძახება 9 + 3
add(34, 8, "*")  # გამოიძახება 34 * 8
add(30, 5, "/")  # გამოიძახება 30 / 5
add(20, 10, "-")  # გამოიძახება 20 - 10
