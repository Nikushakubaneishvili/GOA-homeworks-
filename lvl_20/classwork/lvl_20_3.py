#შეცვალეთ თქვენი დაწერილი ფუნქცია და ჩაუმატეთ return
def add(num1, num2, operation):
    # ამ ფუნქციით შექმნილია კალკულატორის ფუნქცია, რომელიც ასრულებს გამოსახულებას
    # num1 და num2 რიცხვებია, ხოლო operation არის სტრიქონი, რომელიც განსაზღვრავს მოქმედებას (+, -, *, /)
    if operation == "+":
        result=num1 + num2  # დამატება
    elif operation == "-":
        result=num1 - num2  # გამოკლება
    elif operation == "*":
       result=num1 * num2  # გამრავლება
    elif operation == "/":
        result=num1 / num2  # გაყოფა
    else:
        result="Invalid Operation"  # არასწორი ოპერაცია
    return result 

print (add(9, 3, "+"))   # გამოიძახება 9 + 3
print (add(34, 8, "*"))  # გამოიძახება 34 * 8
print (add(30, 5, "/")) # გამოიძახება 30 / 5 
print (add (20, 10, "-") ) # გამოიძახება 20 - 10   