import random

def main():
  targetNumber = random.randint(1, 100)
  guess = 0
  tries = 1

  while (guess != targetNumber):
    guess = int(input("Guess a number (1 - 100): "))

    if guess > targetNumber:
      print(f"Nope! {guess} is too high!\n")
      tries += 1
    elif guess < targetNumber:
      print(f"Nope! {guess} is too low!\n")
      tries += 1
    
  print(f"Correct! You guessed {targetNumber}, in {tries} tries!")

print(main())
