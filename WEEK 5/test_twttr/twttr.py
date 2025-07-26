def main():
  name = input("Input: ").strip()
  print(shorten(name))


def shorten(word):
  result = ""
  for char in word:
    if char not in "aeiouAEIOU":
      result += char
  return result


if __name__ == "__main__":
  main()
