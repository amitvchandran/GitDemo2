# code to open a text file and close

# step1 read the file and store all the lines in list
# step2 Reverse the list
# step3 write the reversed list back to the file

with open('text.txt', 'r') as reader:
    content = reader.readlines()  # all lines will be stored in the list
    reversed(content)  # all lines in the list will be reversed
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
