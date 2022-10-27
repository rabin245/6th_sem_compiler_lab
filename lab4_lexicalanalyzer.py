def isKeyword(word):
    KEYWORDS = ['if', 'else', 'while', 'for', 'int', 'float',
                'char', 'double', 'return', 'break', 'continue', 'void']
    if word in KEYWORDS:
        return True
    else:
        return False


def main():
    # linenumber = 1
    OPERATORS = ['+', '-', '*', '/', '=', '>', '<', '==', '>=', '<=', '!=']

    f = open('lexical.txt', 'r')
    lines = f.readlines()

    for line in lines:
        words = line.split()

        for word in words:
            # remove (), ',' and ';' from word
            word = word.replace('(', '')
            word = word.replace(')', '')
            word = word.replace(',', '')
            word = word.replace(';', '')

            if word in '#include':
                continue
            elif word in OPERATORS:
                print("Operator: ", word)
            elif isKeyword(word):
                print("Keyword: ", word)
            elif word.isidentifier():
                print("Identifier: ", word)
        # linenumber += 1


if __name__ == "__main__":
    main()
