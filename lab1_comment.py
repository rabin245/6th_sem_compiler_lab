def main():
    commentInput = input("Enter a comment: ")
    if commentInput[0] == '/':
        if commentInput[1] == '/':
            print("This is a single line comment")
        elif commentInput[1] == '*':
            if commentInput.endswith('*/'):
                print("This is a multi-line comment")
            else:
                print("This is invalid multi-line comment")
    else:
        print("This is not a comment")


if __name__ == "__main__":
    main()
