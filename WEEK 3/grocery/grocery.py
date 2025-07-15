def main():

  items = {}

  while True:
    try:
      item = input()
      item = item.upper()

      items[item] = items.get(item, 0) + 1

    except EOFError:
      break

  for item in sorted(items.keys()):
    print(f"{items[item]} {item}")

main()

