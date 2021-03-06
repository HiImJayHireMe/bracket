import itertools

from lib.symbols import Symbol


def ara(x, y):
    return all(isa(e, y) for e in x)


def isa(x, y):
    return isinstance(x, y)


def to_string(x):
    return str(x)


def flatten(x):
    if isa(x, list) and len(x) == 0:
        return []
    if isa(x, list):
        return list(itertools.chain(*map(flatten, x)))
    return [x]


class AutoGenSym:
    def __init__(self):
        self.x = 0

    def __call__(self, s=None):
        if s is None:
            return self('')
        x_ = f'{s}{self.x}'
        self.x += 1
        return Symbol(x_)


def munge(s):
    symbols = [('!', '_BANG_'),
               ('+', '_PLUS_'),
               ('-', '_SUB_'),
               ('_*_', '_STAR_'),
               ('/', '_DIV_')]
    for sym, r in symbols:
        s = s.replace(sym, r)
    return s
