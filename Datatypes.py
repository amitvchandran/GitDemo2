
# list in python (array in java)
# list is a data type that allows multiple values
# and can be different data types

values = [1, 2, "rahul", 4.5]

print(values[0])
print(values[2])
print(values[-1])  # gives the last value 4.5 which is only in python
print(values[1:3])  # gives values from 1 to 3 ie 2,rahul and 4.5
values.insert(4, "amit")
print(values)
values.append("end")
print(values)

values[2] = "RAHUL"  # update
del values[0] # delete

print(values)

# Tuple Declaration: same as list but immutable updation is impossible

value = (67, 45, "amit", 90)
print(value[1])

# value[2] = "AVC"
print(value)


# dictionary data type ,flower bracket if string "" , if int no double quotes

dic = {"a": 2, 4: "bcd", "c": "Hello World"}

print(dic[4])
print(dic["c"])

dict = {}
dict["first name"] = "Amit"
dict["last name"] = "Chandran"
print(dict)
print(dict["last name"])


