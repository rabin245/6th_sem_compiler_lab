OPERATORS = ['+', '-', '*', '/', '(', ')']
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2}


def peek(stack):
    return stack[-1]


def infixToPrefix(inputString):
    opStack = []
    expStack = []

    for char in inputString:
        if char.isalpha() and char not in OPERATORS:
            expStack.append(char)
        elif char == '(':
            opStack.append(char)
        elif char == ')':
            while opStack and peek(opStack) != '(':
                op = opStack.pop()
                a = expStack.pop()
                b = expStack.pop()
                expStack.append(op + b + a)
            opStack.pop()
        else:
            while opStack and peek(opStack) != '(' and PRECEDENCE[char] <= PRECEDENCE[peek(opStack)]:
                op = opStack.pop()
                a = expStack.pop()
                b = expStack.pop()
                expStack.append(op + b + a)
            opStack.append(char)

    while opStack:
        op = opStack.pop()
        a = expStack.pop()
        b = expStack.pop()
        expStack.append(op + b + a)

    print('Prefix expression:', expStack[-1])
    return expStack[-1]


def infixToPostfix(inputString):

    outputString = ''
    stack = []

    for char in inputString:
        if char.isalpha() and char not in OPERATORS:
            outputString += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and peek(stack) != '(':
                outputString += stack.pop()
            # pop the '(' remaining in the stack
            stack.pop()
        else:
            while stack and peek(stack) != '(' and PRECEDENCE[char] <= PRECEDENCE[peek(stack)]:
                outputString += stack.pop()
            stack.append(char)

    while stack:
        outputString += stack.pop()

    print('Postfix expressino:', outputString)
    return outputString


def threeAddressCode(finalOperand, postfixExpression):
    stack = []
    i = 1

    for char in postfixExpression:
        if char.isalpha():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            print(f't{i} := {operand1} {char} {operand2}')
            stack.append(f't{i}')
            i += 1
    print(f'{finalOperand} := {stack.pop()}')

    # print('stack', stack)


def main():
    inputString = input("Enter an infix expression: ")
    finalOperand, infixExpression = inputString.split('=')

    prefixExpression = infixToPrefix(infixExpression)
    postfixExpression = infixToPostfix(infixExpression)

    # three address code generation using postfix expression
    print('\nThree address code:\n')
    threeAddressCode(finalOperand, postfixExpression)


if __name__ == '__main__':
    main()
