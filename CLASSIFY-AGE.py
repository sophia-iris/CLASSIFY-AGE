def classify_age(age):
    if age < 0:
        print("Invalid age! Age cannot be negative.")
    elif age <= 12:
        print("You are a Child")
    elif age <= 19:
        print("You are a Teen")
    elif age <= 64:
        print("You are an Adult")
    else:
        print("You are a Senior")

def check():
    age = int(input("Enter your age: "))
    classify_age(age)

check()

while True:
    again = input("mag enter ka pa ba ibang age? (yes or no) ")
    if again == "yes":
        check()
    else:
        print("sigi no na bye")
        break
