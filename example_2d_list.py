grades = [
    [88, 76, 92],
    [95, 89, 90],
    [78, 85, 81]
]

sum = 0

for row in grades:
  for grade in row:
    sum += grade
    print("the grade is: ", grade)
    print("the sum is: ", sum)


# Practice Problem #3

numbers = [
    [5, 15, -2],
    [8, 10, 0],
    [25, -5, 3],
    [100, 9, -1],
    [1, 12]
]

# Create the empty lists here
ten_list = []
zero_thru_nine = []
less_than_zero = []

# Write your nested loops and conditional logic below this line:
for row in numbers:
  for number in row:
    if number > 10:
      ten_list.append(number)
    elif number >= 0 and number < 10:
      zero_thru_nine.append(number)
    else:
      less_than_zero.append(number)

print("Greather than 10:", ten_list)
print("From 0 to 9:", zero_thru_nine)
print("Less than 0:", less_than_zero)
