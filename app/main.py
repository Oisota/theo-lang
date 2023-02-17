import sys

from .lexer import tokenize

def main():
    """Main entry point for the compiler"""
    input_file = sys.argv[1]
    tokens = []
    with open(input_file) as file:
        data = file.read()
        tokens = tokenize(data)

    list(tokens)
    #print(list(tokens))

    #tree = parse(tokens)
    #c_source = emit(tree)

    #with open('./out.c') as out:
    #    out.write(c_source)

def parse(tokens):
    """Parse tokens into AST"""

def transpile(tree):
    """Transpile AST into C source code"""

#if __name__ == '__main__':
#    main()