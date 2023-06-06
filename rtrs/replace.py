from .util import listify, unlistify, dfs, set_path
from .stuff import Variable

def sub_vars(ptn, symbols):
    ptn_as_list = listify(ptn)
    for path, obj in dfs(ptn):
        if isinstance(obj, Variable):
            ptn_as_list = set_path(ptn_as_list, path, symbols[obj.name])
    
    return unlistify(ptn_as_list)

def tree_replace(tree, matches, rule_table):
    tree_as_list = listify(tree)
    for match in matches:
        result = rule_table[match.pattern]
        obj = listify(sub_vars(result, match.symbols))
        tree_as_list = set_path(tree_as_list, match.path, obj)
    
    return unlistify(tree_as_list)
