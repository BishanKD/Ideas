import random 

target = random.randint(1,100)
print("Number is between 1-100")
guess = int(input("Guess the number: "))
attempts = 1
while(guess!=target): 
    if(guess>target):
        guess = int(input("Guess lower: "))
        attempts+=1
    else:
        guess = int(input("Guess higher: "))
        attempts+=1
print(f"Correct. Took {attempts} attempts")
