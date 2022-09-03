#dictionary in python = english to marathi dictionary
#it is collection of key value pairs
#Dict1 = ("key":"value","key2":"value2");
Employee = {
    "name":"shiv",
    "designation":"software",
    "experience":3
}
print(Employee)
print(type(Employee))

"""Dictionary does not allows duplicate keys,if dictionary contains duplicate keys then it is always trys to hold the 
   recent values i.e. Shiv"""  
Employee = {
    "name":"shiv",
    "designation":"software",
    "experience":3,
    "name":"Shiv"
} 
print(Employee)

#Keys with differnt cases are always treated as a different 
#here name and NAME are different
#Keys in dictionary are always case-sentitive
Employee = {
    "name":"shiv",
    "designation":"software",
    "experience":3,
    "NAME":"Shiv",
    "colours": ("red","orange","white")
}
print(Employee)

print(len(Employee))

#Accessing the Dictionary items by using keys
print("colours",Employee["colours"])

#Accessing dictionary items using get() method
print(Employee.get("name"))

#obtaining all the keys using keys() method 
employee_keys = Employee.keys()
print(employee_keys)

#obtaining all the keys using values() method 
employee_values = Employee.values()
print(employee_values)

#changing the values of dictionary
Employee["designation"]="Khatarnak Programmer"
print(Employee["designation"])

#retrieving all the items usimg items() method
employee_items = Employee.items()
print(employee_items)

#cheaking whether the key  exits or not
print("name" in Employee)

#update() method- adding a new value in dictionary
Employee.update({"join year":2020,"salary":50000000})
print(Employee) 

#pop() method-removing a value in dictionary
Employee.pop("salary")
print(Employee)

#removing the last item using popitem() method
Employee.popitem()
print(Employee)

#removing item from dictionary using del keyword
del Employee["colours"]
print(Employee)

#removing all items from dictionary using clear() method
Employee.clear()
print(Employee)

Student ={
    "name":"Gaurav",
    "enroll_no": 2006103,
    "department": "Computer",
    "collage": "GPP"
}
print(Student)

department ={
    "Name":"Computer",
    "Years":3,
    "Subject": ["java","c","c++"]
}
print(department)

student1 = Student.copy()
print(student1)

student1.update(department)
print(student1)

#create dictionary of computer class-nested dictionary
Student_3 ={"Name":"Aditya","Roll no": 103}
computer_class ={
     "Student_1":{"Name":"shiv","Roll no": 101},
     "Student_2":{"Name":"gaurav","Roll no": 102},
     "Student_3": Student_3
}
print(computer_class)
