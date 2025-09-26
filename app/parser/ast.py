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
    pass

@dataclass
class UnaryExpr(Expr):
    operator: str
    expr: Expr

@dataclass
class BinaryExpr(Expr):
    operator: str
    expressions: list = field(default_factory=list)

@dataclass
class BlockExpr(Expr):
    expressions: list = field(default_factory=list)

@dataclass
class Scope(Expr):
    expressions: list = field(default_factory=list)

@dataclass
class FuncDef(Expr):
    name: str
    return_type: str
    params: list = field(default_factory=list)
    expressions: list = field(default_factory=list)

@dataclass
class FuncCall(Expr):
    name: str