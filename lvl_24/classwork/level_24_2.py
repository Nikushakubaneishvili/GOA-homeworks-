def short(list): 
    for short in list: 
        if len(short)>4: 
            list.remove(short) 
    return list
print(short(["ab" ,"abcdgtr"])) 
