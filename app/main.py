import sys

from .lexer import tokenize
from .parser import parse
from .emitter import emit

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
    #print(tree)
    #c_source = emit(tree)

    #with open('./out.c') as out:
        #out.write(c_source)


#if __name__ == '__main__':
#    main()