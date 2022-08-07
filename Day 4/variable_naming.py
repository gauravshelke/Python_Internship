#Valid variable names
'''

myvar = "Shiv" 
my_var = "Shiv"
_my_var = "Shiv"
myVar = "Shiv"
MYVAR = "Shiv"
myvar2 = "Shiv"

#Invalid variable names
2myvar = "Shiv"
my-var = "Shiv"
my var = "Shiv"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

print(2myvar)
print(my-var)
print(my var)
'''

a=45; b="Gaurav" ; c=5.45

print(a)
print(b)
print(c)

#assigning multiple values to multiple variables

col1 ,col2 ,col3 ="red","orange","green"

print(col1)
print(col2)
print(col3)

#assigning one value to multiple variables

col1=col2=col3 ="orange"

print(col1)
print(col2)
print(col3)

#assigning values from list of variables

colours =["red","yellow","orange"]

print("Assigning values from list to variables: ")

col1 ,col2 ,col3 = colours

print(col1)
print(col2)
print(col3)

#printing multiple variables in one print statement

x="Shiv"
y="is"
z="awesome"

print(x + y+ z)
print(x,y,z)

# in case of '+' operator
x=100
y="shiv"
print(x + y)