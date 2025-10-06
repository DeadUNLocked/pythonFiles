weight = float(input("Enter the weight of your container to ship: "))

cost = float(0.00)

if weight <= 0.0:
    cost = 0.00
elif weight <= 2.00:
    cost = 5.00
elif weight <= 6.00:
    cost = 5.00 + 1.50 * (weight - 2.00)
elif weight <= 10.0:
    cost = 11.00 + 1.25 * (weight - 6.00)
else:
    cost = 20.00

print(f"The shipping container is: ${cost:.2f}")
