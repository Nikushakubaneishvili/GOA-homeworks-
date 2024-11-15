def function(list_of_numbers):
    list=[]
    for i in list_of_numbers:
        if i %2 == 0: 
            list.append(i * i) 
        else: 
            list.append(i * 2) 
    return list  
print(function([5,10,15,9,8,4,6,7,1,3])) 
    
