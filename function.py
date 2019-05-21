import re


def openFile(name):
    a = []
    b = []
    file = open(name, 'r')
    strings = file.read()

    for string in strings.split('\n'):
        x, y = (re.split('\s+', string))
        a.append(float(x))
        b.append(float(y))
    return a, b