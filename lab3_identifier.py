def main():
    identifier = input("Enter an identifier: ")
    identifier = identifier.strip()

    if " " in identifier:
        print('Identifier is rejected')
        return

    if identifier[0].isalpha() or identifier[0] == '_':
        if identifier[1:].isalnum() or identifier[1:].find('_') != -1:
            print("Identifier is accepted")
            return
    print('Identifier is rejected')


if __name__ == '__main__':
    main()
