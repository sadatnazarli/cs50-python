import random

def main():
  score = 0
  level = get_level()

  for i in range(10):
    x = generate_integer(level)
    y = generate_integer(level)
    correct_answer = x + y

    for attempt in range(3):
      try:
          answer = int(input(f"{x} + {y} = "))
          if answer == correct_answer:
           score += 1
           break
          else:
            print("EEE")
      except ValueError:
        print("EEE")
    else:
      print(f"{x} + {y} = {correct_answer}")
  print(f"Score: {score}")



def get_level():
  while True:
    try:
      n = int(input("Level: "))
      if n in [1, 2, 3]:
        return n
    except:
      continue


def generate_integer(level):
    if level == 1:
      return random.randint(0, 9)
    elif level == 2:
     return random.randint(10, 99)
    elif level == 3:
      return random.randint(100, 999)
    else:
      raise ValueError

if __name__ == "__main__":
  main()
