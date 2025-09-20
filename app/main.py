import sys

from .lexer import Lexer
from .parser import Parser
from .emitter import Emitter

def main():
    """Main entry point for the compiler"""
    # TODO build out argument parsing
    # EX: theo build f1.theo f2.theo (etc)
    # theo --version
    # theo <sub-command>
    input_file = sys.argv[1]
    tokens = []
    with open(input_file) as file:
        data = file.read()
        lexer = Lexer(data)
        tokens = lexer.lex()

    list(tokens)
    #parser = Parser(tokens)
    #tree = parser.parse()

    #emitter = Emitter(tree)
    #c_source = emitter.emit()

    #with open('./out.c') as out:
        #out.write(c_source)


#if __name__ == '__main__':
#    main()