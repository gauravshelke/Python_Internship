string = "Hello ..!! Welcome to Python"
print(string[0])

# length
print(len(string))

# word search
print("Python" in string)

string_2 = "1,2,3,4,5"
result = "2" in string_2
print(result)

print("8" in string_2)

notinresult = "Programming" not in string
print(notinresult)

# slicing in string
print(string[0:5])

# string slicing from start
print(string[ :32])

#string slicing to the End
print(string[3:])

#negavtive string slicing
print(string[-15:-10])

'''Positive Indexing
E n g i n e e r
0 1 2 3 4 5 6 7
Negative Indexing
E n g i n e e r
-8 -7 - 6 -5 -4  -3 -2 -1'''