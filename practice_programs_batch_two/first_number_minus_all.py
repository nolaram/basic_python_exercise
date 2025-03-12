total = 0

# input ten numbers
for number in range(10):
    difference = int(input(f"\nEnter number {number + 1}: "))

    # subtract all to the first number
    total -= difference
    
# print the difference
print(f"\nThe difference is: {total}")