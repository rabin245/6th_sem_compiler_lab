def main():
    identifier = input("Enter an identifier: ")

    # if identifier.isidentifier():
    #     print("This is a valid identifier")
    #     return

    if identifier[0].isalpha() or identifier[0] == '_':
        if identifier[1:].isalnum() or identifier[1:].find('_') != -1:
            print("Identifier is accepted")
            return
    print('Identifier is rejected')


if __name__ == '__main__':
    main()
