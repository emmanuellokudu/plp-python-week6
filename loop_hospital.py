
# Fixed the ending number to 10 instead of 9
for i in range(1, 11):
    print(i)
    
# Fixed the missing decrement in the while loop
n = 3
while n > 0:
    print(n)
    n -= 1


# Fixed the total variable declaration to be outside the loop instead of inside the loop
total = 0

for i in range(1, 6):
    total = total + i
print(total)