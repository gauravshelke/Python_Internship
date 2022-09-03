

no1 =10
no2 =20
no3 =30
"""
if condition :
    statement  
"""
if no1 > no3 :
    print("No1 is greater than No3")

if no2 < no3 :
    print("No2 is smaller than No3")

#using if-elif
if no1 > no2 :
    print("No1 is greater than No2")
elif no2 > no3 :
    print("No2 is greater than No3")
elif no1 == no2:
    print("No1 is equal to No2")
else :
    print("Wrong Output")

#using if else
if no1 > no3 :
    print("No1 is greater than No3")
else:
    print("No3 is greater than No1")

#short hand if
if no3>no1: print("No3 is greater than No1")

#short if_else
print("No1 is greater than No3") if no1 > no3 else print("No1 is smaller than No3")

#using logical operator  
if no1<no2 and no1<no3 :
    print("No1 is smallet number")

if no1<no2 or no1>no3 :
    print("any one condition is true")




   