count = 0

# input ten numbers
for number in range(10):
    even = int(input(f"\nEnter number {number + 1}: "))

    # check if even number
    if even % 2 == 0:
        count += 1

# print how many is an even number