import random

def main():
  while True:
    try:
      n = int(input("Level: "))
      if n > 0:
        break
    except ValueError:
      pass

  target = random.randint(1, n)

  while True:
    try:
      guess = int(input("Guess: "))
      if guess > 0:
        if guess < target:
          print("Too small!")
        elif guess > target:
          print("Too large!")
        else:
          print("Just Right!")
          break
    except ValueError:
      pass

if __name__ == "__main__":
  main()
