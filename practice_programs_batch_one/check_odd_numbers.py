count = 0

# input ten numbers
for number in range(10):
        odd = int(input(f"\nEnter number {number + 1}: "))

        # check if odd
        if odd % 2 != 0:
                    count += 1

# print how many are the odd numbers