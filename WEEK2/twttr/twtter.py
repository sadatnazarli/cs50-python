def main():
  name = input("Input: ").strip()
  for char in name:
    if char not in "aeiouAEIOU":
      print(char, end= "")
  print()

if __name__ == "__main__":
  main()
