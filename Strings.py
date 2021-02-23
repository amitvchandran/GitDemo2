str = "RahulShettyAcadamy.com"
str1 = "Consulting firm"

str3 = "RahulShetty"

print(str[1]) # output = "a"
print(str[0:5]) # output = "Rahul"

# to concatinate 2 string
print(str + str1)

#if a string is present in another string

print(str3 in str)

#Split String
var = str.split(".")
print(var)
print(var[0])

str4 = "  great  "
print(str4.strip())  # removes white spaces
print(str4.lstrip())  # removes left white spaces
print(str4.rstrip())  # removes right white spaces