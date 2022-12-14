numbers = []
for i in range(5):
    valid = False
    while not valid:
        try:
            number = int(input("Number: "))
            numbers.append(number)
            valid = True
        except ValueError as e:
            print("Not a number. Please re-enter a number.")

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers)/len(numbers):.1f}")

