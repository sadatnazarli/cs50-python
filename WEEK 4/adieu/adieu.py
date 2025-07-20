import inflect

names = []

while True:
  try:
    name = input()
    names.append(name)
  except EOFError:
    break


n = inflect.engine()
formatted_names = n.join(names)
print(f"Adieu, adieu, to {formatted_names}")
