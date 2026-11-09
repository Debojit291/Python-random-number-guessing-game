import random
secret_number= random.randint(1,100)
attempts=0
print("welcome to the random Gussing Game!")
print("you have to select number between 1-100")
while True:
    guess=int(input("Enter your guess:"))
    attempts +=1
    if guess<secret_number:
        print("Too low,try  again")
    elif  guess>secret_number:
        print("Too high,try again")
    else:
        print("Congratulation ! You gussed exact number! ")
        print(f"The secrect number is {secret_number}")
        print(f"number of attempts {attempts}")
        break


