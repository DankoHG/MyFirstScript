# Introduction

intro = 0

while intro == 0:
    confirmation = 0
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    print(f"So, your name is {first_name} {last_name} and you are {age} years old.")
    print("Is this correct? Enter Y or N.")
    answer_1 = input()
    while confirmation == 0:
        if answer_1 in ["Y", "y"]:
            print(f"Perfect, let's continue then, {first_name}.")
            intro = 1
            confirmation = 1
        elif answer_1 in ["N", "n"]:
            print("Let's start again, then.")
            confirmation = 1
        else:
            print("Sorry, I couldn't understand that. Please enter your answer again.")
            print("Enter Y or N.")
            answer_1 = input()
print("SUCCESS")
