inp = input(" Enter the numbers sprated by spaces: ")

numbers = [float(x) for x in inp.split()]

if len(numbers) == 3:
    average = sum(numbers) / len(numbers)

    print("The average is ", average)

else:
    print("Invalid input length")



