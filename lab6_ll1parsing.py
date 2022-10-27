# import firstOf function from lab6_first_follow
from lab5_first_follow import firstOf, followOf


def calculatePrerequisites():
    print("***Note: # is used for epsilon***")
    print("***Note: Use '->' for production. [ E->A|B ]***")
    print(
        "***Note: Only use single letter symbols. [E', id, T', ...] are not accepted.\nReplace with some other symbols [X, i, Y,...]***")

    productions = []
    # productions = [
    #     "E->TX",
    #     "X->+TX|#",
    #     "T->FY",
    #     "Y->*FY|#",
    #     "F->i|(E)"
    # ]
    # productions = [
    #     'E->TB',
    #     'B->+TB|#',
    #     'T->FY',
    #     'Y->*FY|#',
    #     'F->a|(E)'
    # ]
    noOFProductions = int(input("Enter numbers of productions: "))

    print("Enter productions: ")
    for i in range(noOFProductions):
        productions.append(input())

    # input start symbol
    startSymbol = input("Enter start symbol: ")
    # startSymbol = 'E'

    # input terminals
    terminals = []
    # terminals = [
    #     '+',
    #     '*',
    #     'i',
    #     '(',
    #     ')'
    # ]
    noOfTerminals = int(input("Enter numbers of terminals: "))
    print("Enter terminals: ")
    for i in range(noOfTerminals):
        terminals.append(input())

    # input non-terminals
    # nonTerminals = ["E", "X", "T", "Y", "F"]
    # nonTerminals = ['E',
    #                 'B',
    #                 'T',
    #                 'Y',
    #                 'F']
    nonTerminals = []
    noOfNonTerminals = int(input("Enter numbers of non-terminals: "))
    print("Enter non-terminals: ")
    for i in range(noOfNonTerminals):
        nonTerminals.append(input())

    # convert productions to dictionary
    productionsDict = {}

    for production in productions:
        production = production.split("->")
        productionsDict[production[0]] = production[1].split("|")

    terminalProductions = {}
    for terminal in terminals:
        for symbol, prods in productionsDict.items():
            for prod in prods:
                if terminal in prod:
                    terminalProductions[symbol, terminal] = prod

    # print(terminalProductions)
    # print(productionsDict)

    # initialize first and follow
    first = {}
    follow = {}

    for nonTerminal in nonTerminals:
        first[nonTerminal] = set()
        follow[nonTerminal] = set()

    for nonTerminal in nonTerminals:
        first[nonTerminal] = first[nonTerminal] | firstOf(
            nonTerminal, productionsDict, nonTerminals, terminals)

    for nonTerminal in nonTerminals:
        follow[nonTerminal] = follow[nonTerminal] | followOf(
            nonTerminal, productionsDict, nonTerminals, terminals, startSymbol, first)

    print("\nGrammar:")
    for prod in productions:
        print(prod)

    print('\n\n{:15} {:15} {:15}'.format('Non-Terminal', 'First', 'Follow'))
    print('-'*55)
    for nonTerminal in nonTerminals:
        print('{:15} {:15} {:15}'.format(nonTerminal,
              str(first[nonTerminal]), str(follow[nonTerminal])))
    print('-'*55)
    return startSymbol,  productionsDict, first, follow, terminalProductions


def ll1Table(productionDict, first, follow, terminalProductions):
    table = dict()

    for key, productions in productionDict.items():
        # get the first of current production without epsilon
        firstOfProduction = first[key] - {'#'}
        for production in productions:
            # if the production is not epsilon then
            # add the production to the production to corresponding first of key
            if production != '#':
                for terminal in firstOfProduction:
                    if (key, terminal) not in table:
                        # this is to make sure that the productions with terminal symbols
                        # are added to the correct 'terminal' column in the table
                        # i.e. if the production is 'i' then it should be added to the 'i' column
                        # and not to the '(' column
                        if (key, terminal) in terminalProductions:
                            table[key, terminal] = terminalProductions[key, terminal]
                            continue
                        # if the production is not a terminal symbol then simply add it to the table under the corresponding first of key
                        table[key, terminal] = production
            # if the production is epsilon then add the (epsilon) production to the follow of key
            else:
                for terminal in follow[key]:
                    table[key, terminal] = production

    print('\nParsing table:')
    print("{:35}{:15}".format('(Non-Terminal, Terminal)', 'Production'))
    print('-'*40)
    for key in table:
        # print(key, table[key])
        print("{:35}{:15}".format(str(key), table[key]))
    print('-'*40)

    return table


def parser(inputString, startSymbol, parsingTable):
    # initialize stack
    stack = []
    stack.append('$')
    stack.append(startSymbol)

    # initialize input
    inputString = inputString + '$'

    print('\n{:15} {:15}'.format('Stack', 'Input'))
    print('-'*30)
    while len(stack) > 0:
        print('{:15} {:15}'.format(
            ''.join(stack), inputString))

        topOfStack = stack.pop()

        # if stack is empty
        if topOfStack == '$':
            print('-'*30)
            print("\nString is accepted")
            break
        # if top of stack matches with input string
        elif topOfStack == inputString[0]:
            inputString = inputString[1:]
        # if top of stack is non-terminal
        else:
            try:
                production = parsingTable[topOfStack, inputString[0]]
                if production == '#':
                    continue
                else:
                    for i in range(len(production) - 1, -1, -1):
                        stack.append(production[i])
            # if no production found for corresponding top of stack and input string in the parsing table
            except KeyError:
                print('-'*30)
                print("\nString is not accepted")
                break


def main():
    startSymbol, productionDict, first, follow, terminalProductions = calculatePrerequisites()

    # parsing table
    parsingTable = ll1Table(
        productionDict, first, follow, terminalProductions)

    # input string
    inputString = input("\nEnter input string: ")

    # parse input string
    parser(inputString, startSymbol, parsingTable)


if __name__ == "__main__":
    main()
