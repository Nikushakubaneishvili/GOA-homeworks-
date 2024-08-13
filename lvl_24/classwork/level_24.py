def even (list): 
    for even in list:
        if even %2==0: 
            list.remove(even) 
    return list 
print (even([1,2,3,4,5,6])) 
