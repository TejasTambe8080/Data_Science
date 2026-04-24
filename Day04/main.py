with open("Data.txt", "r") as file:
    numbers = file.readlines()

numbers = [int(num.strip()) for num in numbers]
total = sum(numbers)

print("Numbers:", numbers)
print("Total Sum:", total)