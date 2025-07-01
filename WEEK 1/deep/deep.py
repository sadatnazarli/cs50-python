def main():
  number = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
  if (number == "42"):
    print("Yes")
  elif (number == "forty two"):
    print("Yes")
  elif (number == "forty-two"):
    print("Yes")
  else:
    print("No")

main()

