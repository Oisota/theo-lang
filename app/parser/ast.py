from dataclasses import dataclass, field

@dataclass
class Program:
    imports: list = field(default_factory=list)
    expressions: list = field(default_factory=list)

@dataclass
class Import:
    path: str = ''
    qualifier: str = ''