def main():
  fuel = input("Fraction: ")
  try:
    percentage = convert(fuel)
    result = gauge(percentage)
    print(result)
  except (ValueError, ZeroDivisionError):
    main()


def convert(fraction):
  parts = fraction.split("/")
  x = int(parts[0])
  y = int(parts[1])

  if y == 0:
    raise ZeroDivisionError
  elif x > y or x < 0 or y < 0:
    raise ValueError
  else:
    percentage = (x / y) * 100
    return round(percentage)

def gauge(percentage):
  if percentage <= 1:
    return "E"
  elif percentage >= 99:
    return "F"
  else:
    return f"{percentage}%"


if __name__ == "__main__":
  main()
