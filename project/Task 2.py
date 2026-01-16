import random

password = input("Enter your password: ")

if len(password) < 9:
    print("Password too short.")
    exit()

for _ in range(3):
    position = random.randint(1, len(password))
    guess = input(f"Enter letter at position {position}: ")

    if guess == password[position - 1]:
        print("Correct")
    else:
        print("Security check failed.")
        exit()

print("Security check passed.")
