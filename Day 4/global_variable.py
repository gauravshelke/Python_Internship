from ast import Global


Name ="Shiv"
def myfunc():
 #print("My name is :" + Name)

 global Name
 Name="ABC"
 print(Name)
myfunc()

print("My name is :" + Name)

