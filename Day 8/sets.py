#set is a collection of unique values
set1 = {"Apple", "Mango", "Banana", "Apple",10, 20.5}
print(set1)

print(len(set1))

#set constructor
set_constructor = set(("Pink", "Black", "White"))
print(set_constructor)

print("Pink" in set_constructor)

#for loop
for color in set_constructor:
    print(color)

#using add() method
set_constructor.add("Yellow")
print(set_constructor)

# set_constructor.add("Purpule", "Blue", "Sky")

#update() method
set2 = {1,2,3,4,5}
set_constructor.update(set2)
print(set_constructor)

list1 = {11,22,33,44,55,66}
set_constructor.update(list1)
print(set_constructor)

#remove() method
set_constructor.remove(11)
set_constructor.remove("Yellow")
#it will through error
#set_constructor.remove("Yellow")
print(set_constructor)

#it will not through error
set_constructor.discard("Yellow")
print(set_constructor)

#remove last element of the set
books = {"Java", "c++", "python", "c"}
print(books.pop())
print(books)

books.clear()
print(books)

del books
# print(books)

#union() method
numbers = {101,102,103,104,105,101}
strings = {"Shankar","Pranav","Gaurav","Shankar",101,102}
combine_set = numbers.union(strings)
print(combine_set)

numbers.intersection_update(strings)
print(numbers)

duplicate_values = numbers.intersection(strings)
print(duplicate_values)

numbers.symmetric_difference_update(strings)
print(numbers)
