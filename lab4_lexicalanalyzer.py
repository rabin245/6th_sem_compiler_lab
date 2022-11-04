def isKeyword(word):
    KEYWORDS = ['if', 'else', 'while', 'for', 'int', 'float',
                'char', 'double', 'return', 'break', 'continue', 'void']
    if word in KEYWORDS:
        return True
    else:
        return False


def main():
    OPERATORS = ['+', '-', '*', '/', '=', '>', '<', '==', '>=', '<=', '!=']

    f = open('lexical.txt', 'r')
    lines = f.readlines()

    operators = []
    keywords = []
    identifiers = []
    constInts = []

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
                operators.append(word)
            elif isKeyword(word):
                keywords.append(word)
            elif word.isidentifier():
                identifiers.append(word)
            elif word.isnumeric():
                constInts.append(word)

    print('Keywords:')
    for i in set(keywords):
        print(i, end=' ')
    print('\n')
    print('Identifiers:')
    for i in set(identifiers):
        print(i, end=' ')
    print('\n')
    print('Operators:')
    for i in set(operators):
        print(i, end=' ')
    print('\n')
    print('Constant Ints:')
    for i in set(constInts):
        print(i, end=' ')
    print('\n')


if __name__ == "__main__":
    main()
