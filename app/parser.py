"""Parser Code

Parse the token stream into an AST
"""
from .processor import Processor
from .ast import Import
from .token import Token, TokenType
from .tokens import Keywords, Syntax

class Parser(Processor):
    """Class responsible for parsing token list into program AST"""

    def parse(self):
        """Parse tokens into AST"""
        tree = self.parse_program()
        return tree

    def parse_program(self):
        """Parse tokens into AST"""
        tree = ast.Program()
        tree.imports = self.parse_imports(tree, self.data)
        return tree

    def parse_imports(self):
        """Parse import list"""
        imports = []

        self.match(Keywords.IMPORT)
        self.match(Syntax.PAREN_OPEN)

        while self.current.type != TokenType.PAREN_CLOSE:
            # parse import path
            if self.current.type == TokenType.STRING:
                imp = Import(self.current.value, self.current.value.split('/')[-1])
                self.next()

                if self.current.type == TokenType.IDENTIFIER:
                    imp.name = self.current.value
                    self.next()
                elif self.current.type == TokenType.PAREN_OPEN:
                    self.match(Syntax.PAREN_OPEN)
                    while self.current.type == TokenType.IDENTIFIER:
                        imp.items.append(self.current.value)
                        self.next()
                    self.match(Syntax.PAREN_CLOSE)

                imports.append(imp)
            else:
                # TODO probably need some kind of error message or exception
                break

        self.match(Syntax.PAREN_CLOSE)

        return imports

    def match(self, expected: Token):
        if self.current.matches(expected):
            self.next()