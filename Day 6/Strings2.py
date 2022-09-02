'''___Program for string modification functions___'''

name = "My name is PRANAV"
print(name.lower())

name = "snehal"
print(name.upper())

name = "LALALALALALALALLALALALALAA"
print(name.lower())

name = '''                                                         this string containg whitespaces  
                               but why i dont know so that  i am removing it using strip() method                                                                   '''
print(name.strip())

paragraph = " hey how are you, are you doing a wrong code, oops you must be replaced by using replace() method"
print(paragraph.replace("h", "o"))

team = "hello, team, pranav, gourav, snehal, vaishnavi, pratiksha, ganesh, we must split by any operator"
print(type(team))
team_list = team.split(",")
print(team_list)
#['hello', ' team', ' pranav', ' gourav', ' snehal', ' vaishnavi', ' pratiksha', ' ganesh', ' we 
#must split by any operator']
print(type(team_list))
print(team.split("."))

#Concatenation of string

str1 = "Python"
str2 = "Intership"

#concatenating strings
result = str1 + str2
print(result)

space = " "
result = str1 + space + str2
print(result)

#String format method

name = "my name is Priti, and I am {} years old, I like {}, My college is {}"
print(name.format(17, "Chocolates", "GPP"))


print(name.capitalize())


print(bool())
print(bool("is this true"))
print(bool(1234))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(False))
print(bool(None))

