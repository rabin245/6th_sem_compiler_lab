def firstOf(nonTerminal, productionsDict, nonTerminals, terminals):
    firstSet = set()

    # loop over the production of nonTerminal symbol
    for production in productionsDict[nonTerminal]:
        if production == '#':
            firstSet = firstSet | {'#'}
        elif production[0] in terminals:
            firstSet = firstSet | {production[0]}
        elif production[0] in nonTerminals:
            firstSet = firstSet | firstOf(
                production[0], productionsDict, nonTerminals, terminals)

    return firstSet


def followOf(
        nonTerminal, productionsDict, nonTerminals, terminals, startSymbol, first):
    followSet = set()

    # if nonTerminal is start symbol
    if nonTerminal == startSymbol:
        followSet = followSet | {'$'}

    for nonTerm, productions in productionsDict.items():
        for production in productions:
            if nonTerminal in production:
                index = production.index(nonTerminal)
                if index == len(production) - 1:
                    if nonTerm != nonTerminal:
                        followSet = followSet | followOf(
                            nonTerm, productionsDict, nonTerminals, terminals, startSymbol, first)
                else:
                    nextSymbol = production[index + 1]
                    if nextSymbol in terminals:
                        followSet = followSet | {nextSymbol}
                    elif nextSymbol in nonTerminals:
                        # firstSet = firstOf(
                        #     nextSymbol, productionsDict, nonTerminals, terminals)
                        firstSet = first[nextSymbol]
                        if '#' in firstSet:
                            followSet = followSet | (firstSet - {'#'})
                            followSet = followSet | followOf(
                                nonTerm, productionsDict, nonTerminals, terminals, startSymbol, first)
                        else:
                            followSet = followSet | firstSet

    return followSet


def main():

    # input productions
    productions = []
    # productions = [
    #     'E->TB',
    #     'B->+TB|#',
    #     'T->FY',
    #     'Y->*FY|#',
    #     'F->a|(E)'
    # ]
    noOFProductions = int(input("Enter numbers of productions: "))

    print("***Note: # is used for epsilon***")
    print("***Note: Use '->' for production. [ E->A|B ]***")
    print(
        "***Note: Only use single letter symbols. [E', id, T', ...] are not accepted.\nReplace with some other symbols [X, i, Y,...]***")
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
    #     'a',
    #     '(',
    #     ')'
    # ]
    noOfTerminals = int(input("Enter numbers of terminals: "))
    print("Enter terminals: ")
    for i in range(noOfTerminals):
        terminals.append(input())

    # input non-terminals
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

    # print("First: ")
    # print(first)

    for nonTerminal in nonTerminals:
        follow[nonTerminal] = follow[nonTerminal] | followOf(
            nonTerminal, productionsDict, nonTerminals, terminals, startSymbol, first)

    # print('Follow: ')
    # print(follow)

    # print(terminals)
    print('{:15} {:15} {:15}'.format('Non-Terminal', 'First', 'Follow'))
    for nonTerminal in nonTerminals:
        print('{:15} {:15} {:15}'.format(nonTerminal,
              str(first[nonTerminal]), str(follow[nonTerminal])))


if __name__ == "__main__":
    main()


# production
# E->TB
# B->+TB|#
# T->FY
# Y->*FY|#
# F->a|(E)

# terminals
# +
# *
# a
# (
# )

# non terminals
# E
# B
# T
# Y
# F
