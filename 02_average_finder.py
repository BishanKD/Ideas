def average(numbers):
    return sum(numbers)/ len(numbers)

count = int(input("Enter number of values: "))
list = []
for i in range(count):
    value = int(input("Enter number: "))
    list.append(value)
print(f"The average is {average(list)}")
