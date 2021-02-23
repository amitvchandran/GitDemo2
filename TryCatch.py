#try

# To Print customised exception message
try:
    with open('text.txt', 'r') as reader:
        reader.read()

except:  # in python instaed of catch we have except
    print("somehow i reached because there is failure in try block")

# To Print  exception message given by python

try:
    with open('text.txt', 'r') as reader:
        reader.read()

except Exception as e: # in python instaed of catch we have except
    print(e)

# FINALLY keyword
# this will run no matter if u have pass/failure in try catch mechanism

try:
    with open('text.txt', 'r') as reader:
        reader.read()

except Exception as e: # in python instaed of catch we have except
    print(e)

finally:
    print("this will run no matter if u have pass/failure in try catch mechanism")

