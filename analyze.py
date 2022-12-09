def charWasAnalyzed(char, analyzes):
    for analyze in analyzes:
        if analyze[0] == char:
            return True
    return False


def returnsProminent(string):
    analyzes = analyzeChars(string)
    char = ''
    length = 0
    for analyze in analyzes:
        if analyze[1] > length:
            char = analyze[0]
            length = analyze[1]
    return char, length


def analyzeChar(char, string):
    length = 0
    for c in string:
        if c == char:
            length += 1
    return char, length


def analyzeChars(string):
    analyzes = []
    for char in string:
        if not charWasAnalyzed(char, analyzes):
            analyze = analyzeChar(char, string)
            analyzes.append(analyze)
    return analyzes


string = input('string: ')
try:
    prominent = returnsProminent(string)
    print(prominent)
except:
    print('Houve algum erro...')
