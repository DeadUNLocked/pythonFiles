# Write a nested loop that iterates through the grades list below. Your code should calculate and print the sum of all the numbers in the list.

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
