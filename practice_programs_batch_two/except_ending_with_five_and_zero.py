# print zero to one hundred
for number in range(101):
    # check if ending with five or zero
    if number % 10 != 5 and number % 10 != 0:
        # print the number
        print(number)