"""Parser Code

Parse the token stream into an AST
"""
from app.parser.ast import Import
from app.lexer.token import Token, TokenType
from app.tokens import Keywords, Syntax

class Parser:
    """Class responsible for parsing token list into program AST"""
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.consumed = 0

    @property
    def current(self):
        return self.tokens[self.consumed]

    def parse(self):
        """Parse tokens into AST"""
        tree = self.parse_program()
        return tree

    def parse_program(self):
        """Parse tokens into AST"""
        tree = ast.Program()
        tree.imports = self.parse_imports(tree, tokens)
        return tree

    def parse_imports(self):
        """Parse import list"""
        imports = []

        self.match(Keywords.IMPORT)
        self.match(Syntax.PAREN_OPEN)

        while self.current.type != TokenType.PAREN_CLOSE:
            # parse import path
            if self.current.type == TokenType.STRING:
                imp = Import(self.current.value)
                self.next()

                if self.current.type in (TokenType.OPERATOR, TokenType.IDENTIFIER):
                    imp.qualifier = self.current.value
                    self.next()

                imports.append(imp)
            else:
                # TODO probably need some kind of error message or exception
                break

        self.match(Syntax.PAREN_CLOSE)

        return imports

    def match(self, expected: Token):
        if self.current.matches(expected):
            self.next()

    def next(self):
        self.consumed += 1