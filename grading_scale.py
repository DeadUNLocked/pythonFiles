score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score <= 90:
    print("Grade: B")
elif score >= 70 and score <= 80:
    print("Grade: c")
elif score >= 60 and score <= 70:
    print("Grade: D")
elif score >=100:
    print("Grade: INVALID")
elif score <= 0:
    print("Grade: IMPOSSIBLE")
else:
    print("Grade: F")