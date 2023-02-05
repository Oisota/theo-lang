import sys

from tokenize import tokenize

def main():
    """Main entry point for the compiler"""
    input_file = sys.argv[1]
    with open(input_file) as file:
        tokens = tokenize(file.read())

    print(tokens)

    #tree = parse(tokens)
    #c_source = transpile(tree)

    #with open('./out.c') as out:
    #    out.write(c_source)

def parse(tokens):
    """Parse tokens into AST"""

def transpile(tree):
    """Transpile AST into C source code"""

if __name__ == '__main__':
    main()