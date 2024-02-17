from sys import stdin;
from parser.Parser import Parser;


if __name__ == '__main__':

    parser = Parser()
    parser.setParser()

    for line in stdin:
        if line.strip("\n "):
            parser.parseLine(line.strip("\n "))

    print(parser.refactoryHTML())