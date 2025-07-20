import emoji


def main():
    text = input()
    result = emoji.emojize(text, language='alias')
    print(result)


main()
