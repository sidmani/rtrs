from pprint import pprint
from .stuff import Variable, Symbol 
from .match import tree_match
from .replace import tree_replace
import pdb

S = Symbol("S")
K = Symbol("K")
I = Symbol("I")
a = Variable("a")
b = Variable("b")
c = Variable("c")

I_RULE = [(I, a), a]
K_RULE = [((K, a), b), a]
S_RULE = [(((S, a), b), c), ((a, c), (b, c))]

def run():
    rules = [I_RULE, K_RULE, S_RULE]
    rule_table = {l:r for [l, r] in rules}

    matches = [0]
    expr = (((S, I), I), K)
    while len(matches) > 0:
        print(expr)
        matches = tree_match(expr, [r[0] for r in rules])
        print(matches)
        if len(matches) > 0:
            expr = tree_replace(expr, [matches[0]], rule_table)
    pprint(expr)

if __name__ == "__main__":
    run()
