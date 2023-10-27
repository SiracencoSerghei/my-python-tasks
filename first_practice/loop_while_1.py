#!/usr/bin/python3

secret = 20
attempt = -1
counter = 1
found = False

# while secret != attempt:
#     attempt = int(input('guess: '))
#     if attempt == 0:
#         print("Bye!")
#         break
# else:
#     print(f'You are guessed right!!!\n you did it in {counter} tries ')
# print("we are came out from loop")
    
while (attempt := int(input('guess: '))) != secret:
    if attempt == 0:
        print("Bye!")
        break
    if not found:
        print("You didn't guess the secret number.")
else:
    found = True
    print('Congratulations, you guessed the secret number!')


print("We came out of the loop.")