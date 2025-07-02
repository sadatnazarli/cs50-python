def main():
  num = input("Expression: ").strip()
  x, y, z = num.split()

  x = float(x)
  z = float(z)

  if (y == "+"):
    print(x + z)
  elif (y == "-"):
    print(x - z)
  elif (y == "*"):
    print(x * z)
  elif (y == "/"):
    print(x / z)
  else:
    exit()

main()
