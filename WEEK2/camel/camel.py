def main():
  name = input("camelCase: ")
  result = ""
  for i in range(len(name)):
    if name[i].isupper() and i != 0:
      result += "_"
      result += name[i].lower()
    else:
      result += name[i].lower()

  print(result)

if __name__ == "__main__":
    main()
