def main():
    print('***Note: Separate each production into a new line***')
    print('***Note: Production of form [ S->S+S ]***')
    print(
        "***Note: Only use single letter symbols. [E', id, T', ...] are not accepted.\nReplace with some other symbols [X, i, Y,...]***")

    # productions = [
    #     'S->S+S',
    #     'S->S*S',
    #     'S->i',
    # ]
    productions = list()
    noOfProductions = int(input("\n\nEnter the number of productions: "))
    for i in range(noOfProductions):
        productions.append(input())

    startSymbol = input("Enter the start symbol: ")
    # startSymbol = 'S'

    productionList = list()
    for production in productions:
        production = production.split("->")
        productionList.append({production[0]: production[1]})
    # print(productionList)

    inputString = input("Enter the input string: ")

    stack = '$'
    print("{:15} {:15} {:15}".format("Stack", "Input", "Action"))
    print('-'*50)
    print("{:15} {:15} {:15}".format(stack, inputString+'$', "Initial"))
    while True:
        reduceFlag = False
        action = ''

        if stack == f'${startSymbol}' and len(inputString) == 0:
            print('-'*50)
            print('String Accepted')
            break
        else:
            for prod in productionList:
                for key, value in prod.items():
                    if stack.endswith(value) and reduceFlag is False:
                        stack = stack[:-len(value)]
                        stack += key
                        reduceFlag = True
                        break
            if reduceFlag is False:
                if len(inputString) == 0:
                    print('-'*50)
                    print('String Rejected')
                    break
                stack += inputString[0]
                inputString = inputString[1:]
        action = 'Reduce' if reduceFlag is True else 'Shift'

        print("{:15} {:15} {:15}".format(stack, inputString+'$', action))


if __name__ == '__main__':
    main()
