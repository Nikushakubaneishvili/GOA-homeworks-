#Check if a given string entered by the user is a palindrome
word=input("please enter palindrome: ")
if word==word[::-1] :
  print("word is palindrome")
else: 
  print("word is not palindrome")