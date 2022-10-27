import re


def main():
    f = open('comment.txt', 'r')

    validCount = 0
    lineNumber = 1
    invalidMultilineCommentLine = 0
    multilineFlag = False

    lines = f.readlines()
    for line in lines:
        if re.search(r'//', line) and not multilineFlag:
            print(lineNumber, line)
            validCount += 1
        elif re.search(r'/\*', line) and not multilineFlag:
            multilineFlag = True
            invalidMultilineCommentLine = lineNumber
            print(lineNumber, line)
        if multilineFlag is True:
            if re.search(r'\*/$', line):
                multilineFlag = False
                print(lineNumber, line)
                validCount += 1

        lineNumber += 1

    if multilineFlag is True:
        print("Invalid multi-line comment at line", invalidMultilineCommentLine)

    print("Valid comments: ", validCount)


if __name__ == '__main__':
    main()
