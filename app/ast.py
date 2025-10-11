from dataclasses import dataclass, field

@dataclass
class Program:
    imports: list = field(default_factory=list)
    expressions: list = field(default_factory=list)

@dataclass
class Import:
    path: str = ''
    name: str = '' # package name, or alias if given
    items: list = field(default_factory=list) # specific items to import if any

@dataclass
class Expr:
    """Base expression class"""

@dataclass
class UnaryExpr(Expr):
    operator: str
    expr: Expr

@dataclass
class BinaryExpr(Expr):
    operator: str
    operand1: Expr
    operand2: Expr 

@dataclass
class ExprList(Expr):
    expressions: list = field(default_factory=list)

@dataclass
class BlockExpr(ExprList):
    pass

@dataclass
class Scope(ExprList):
    params: list = field(default_factory=list)

@dataclass
class FuncDef(Expr):
    name: str
    return_type: str
    params: list = field(default_factory=list)
    block: BlockExpr
    anonymous: bool

@dataclass
class FuncCall(Expr):
    name: str