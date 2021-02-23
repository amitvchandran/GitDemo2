
# IF ELSE condition

greeting = "Good morning"

if greeting == "Good morning":
    print("condition Matches")
    print("second line")
else:
    print("condition do not match")

print("IF ELSE...It is completed")

# for loop

obj = [2, 3, 4, 5, 6, 7, 8]
for i in obj:
    print(i)
    print(i*2)  # tp print multiples of 2

# sum of first 5 natural numbers 1+2+3+4+5=15
summation = 0
for j in range(1, 6):  # range(i,j) => i to j-1
    summation = summation + j
print(summation)

# new one for iteration k++ (here +2)
for k in range(1, 10, 2):
    print(k)
    print("**********Skipping first index************")
for m in range(10):
    print(m)

# WHILE LOOP

print("#############while loop###################")

it = 4

while it > 1:
    print(it)
    it = it - 1

print("while loop execution is done")

print("#############while loop not to print 3###################")
it = 4
while it > 1:
    if it != 3:
        print(it)

    it = it - 1

print("while loop execution is done")

# BREAK
print("#############while loop with break###################")

it = 10
while it > 1:
    if it == 3:
        break
    print(it)

    it = it - 1

print("while loop execution is done")

# CONTINUE
print("#############while loop with continue###################")

it = 10
while it > 1:
    if it == 9:
        it = it-1
        continue
    if it == 3:
        break
    print(it)

    it = it - 1