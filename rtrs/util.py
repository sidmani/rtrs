def listify(tup):
    if not isinstance(tup, tuple):
        return tup

    return list(map(lambda x: listify(x) if isinstance(x, tuple) else x, tup))


def unlistify(lst):
    if not isinstance(lst, list):
        return lst

    return tuple(map(lambda x: unlistify(x) if isinstance(x, list) else x, lst))


def get_path(tree, path):
    obj = tree
    for i in path:
        obj = obj[i]
    return obj


# note that this only works on lists
def set_path(tree, path, val):
    if path == ():
        return val

    obj = tree
    for i in path[:-1]:
        obj = obj[i]
    obj[path[-1]] = val

    return tree


def dfs(tree):
    q = [()]
    while len(q) > 0:
        nxt = q.pop()
        nxt_obj = get_path(tree, nxt)
        yield nxt, nxt_obj

        # add all children of nxt to q
        if isinstance(nxt_obj, tuple):
            q = [nxt + (len(nxt_obj) - idx - 1,) for idx, _ in enumerate(nxt_obj)] + q
