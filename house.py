name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case _:
        print("Who? ")