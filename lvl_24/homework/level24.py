def long_strings(list):
 long = list[0] 
 for i in list:
  if len (i) > len (long):
   long=i  
 return long

print(long_strings(["nika", "shalva", "mercedesi", "astonmartini"]))  
 