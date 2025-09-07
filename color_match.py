users = [
    ["Aiden", "yellow"], 
    ["Elliott", "green"],
    ["Jaydon", "blue"],
    ["Joshua", "red"],
    ["Ryan", "orange"]
]


matched = False

name = input("Please enter your name: ")
print(f"Hello, {name}!")

color = input("What is your favorite color? (use lowercase only) ")
print(f"Your favorite color is {color}.")

index = 0

while index < len(users):
    if color == users[index][1]:
        print(f"Your favorite colors are identical to {users[index][0]}.")
        matched = True
        break
    index += 1

if matched == False:
   print("Match not found")
