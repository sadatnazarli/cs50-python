from pyfiglet import Figlet
import sys
import random

def main():
  figlet = Figlet()
  fonts = figlet.getFonts()

  if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
  elif len(sys.argv) == 3: # 1 programin  adi yeni figlet.py 2 -f yada --font 3 font name olacaq
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
      figlet.setFont(font=sys.argv[2])
    else:
      sys.exit(1)
  else:
    sys.exit(1)

  text = input("Input: ")
  print(figlet.renderText(text))


if __name__ == "__main__":
  main()
