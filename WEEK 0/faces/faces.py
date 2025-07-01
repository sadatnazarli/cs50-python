def main():
  name = input().strip()
  print(convert(name))

def convert(text):
 text = text.replace(':)', '🙂')
 text = text.replace(':(', '🙁')
 return text

main()
