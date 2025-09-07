users = [
    ["Aiden", "yellow"], 
    ["Elliott", "green"],
    ["Jaydon", "blue"],
    ["Joshua", "red"],
    ["Ryan", "blue"]
]

print(users[0][1])
print(users[2][0])


name = input("Please enter your name: ")
print(f"Hello, {name}!")

color = input("What is your favorite color? ")
print(f"Your favorite color is {color}.")

index = 0

while index < len(users): # Check against the *current* length
  if color == users[index][1]:
    print(f"Your favorite colors are identical to {users[index][0]}.")
    break
