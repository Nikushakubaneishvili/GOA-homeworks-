num = 5

# print(True and True) # True        #and ოპერატორი აბრუნებს trues თუ ორივე პირობისთვის მოცემული მნიშვნელობა ჭეშმარიტია
# print(True and False) # False      #ხოლო false თუ ერთისთვისაა მოცემული. 
# print(False and True) # False
# print(False and False) # False 

# print(True or True) # True
# print(True or False) # True         #or ოპერატორი აბრუნებს trues თუ ერთ ერთი პირობისთის მოცემული მნიშვნელობა
# print(False or True) # True         #ჭეშმარიტია, ხოლო false თუ ორივესთვისაა მიცემული 
# print(False or False) # False

print("----------- AND -----------")

print(num >= 1 and num <= 10) # True        
print(num >= 1 and num <= 4) # False
print(num > 5 and num <= 10) # False
print(num > 5 and num > 10) # False

print("----------- OR -----------")

print(num >= 1 or num <= 10) # True
print(num >= 1 or num <= 4) # True
print(num > 5 or num <= 10) # True
print(num > 5 or num > 10) # False