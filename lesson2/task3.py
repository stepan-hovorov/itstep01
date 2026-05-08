import random

print("---Guess my number---")
print("You have 3 attempts")
print("Number is in range 1 and 10")
magic_number = random.randint(1, 10)
count = 0
user_number = 0
while count < 3:
    print(f'your attempt:{count + 1}')
    user_number = int(input("Your number: "))
    count += 1

    if magic_number > user_number:
        print("Your guess is too low")

    elif magic_number < user_number:
        print("Your guess is too hige")

    else:
        print("You win. It on the", count, )
        break
if user_number != magic_number:
    print("you lost this game")
import random

print("---Guess my number---")
print("You have 3 attempts")
print("Number is in range 1 and 10")
magic_number = random.randint(1, 10)
count = 0
user_number = 0
while count < 3:
    print(f'your attempt:{count + 1}')
    user_number = int(input("Your number: "))
    count += 1

    if magic_number > user_number:
        print("Your guess is too low")

    elif magic_number < user_number:
        print("Your guess is too hige")

    else:
        print("You win. It on the", count, )
        break
if user_number != magic_number:
    print("you lost this game")
