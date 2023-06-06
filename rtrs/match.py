from collections import namedtuple
from .stuff import Variable, Symbol
from .util import dfs

Match = namedtuple("Match", ["pattern", "path", "symbols"])

def normalize_path(base, path):
    if len(path) < len(base):
        return None
    if len(path) == len(base):
        if path == base:
            return ()
        return None

    if path[: len(base)] == base:
        return path[len(base) :]
    return None


# returns list of pairs (pattern, path)
def tree_match(tree, ptns):
    filteredPatterns = []
    for path, vertex in dfs(tree):
        # add all patterns as potentially being rooted at this vertex
        filteredPatterns += [Match(p, path, dict()) for p in ptns]

        # filter out the ones that don't match at this particular path
        failed = set()
        for idx, (ptn, ptnRootPath, ptnSymbols) in enumerate(filteredPatterns):
            normalPath = normalize_path(ptnRootPath, path)
            if normalPath is None:
                # the pattern doesn't overlap with this vertex
                continue

            # extract the relevant portion of the pattern
            ptnObj = ptn
            skip = False
            for p in normalPath:
                if isinstance(ptnObj, Variable):
                    # the current portion of the target is inside a variable
                    skip = True
                elif isinstance(ptnObj, Symbol):
                    raise Exception("I thought this shouldn't happen")
                else:
                    ptnObj = ptnObj[p]

            if skip:
                continue

            # try to match the pattern object to the current vertex
            if isinstance(ptnObj, tuple):
                # the vertex must be a tuple of the same length
                if not isinstance(vertex, tuple) or len(vertex) != len(ptnObj):
                    failed.add(idx)
            elif isinstance(ptnObj, Variable):
                if ptnObj.name in ptnSymbols and ptnSymbols[ptnObj.name] != vertex:
                    failed.add(idx)
                else:
                    ptnSymbols[ptnObj.name] = vertex
            elif ptnObj != vertex:
                failed.add(idx)

        filteredPatterns = [
            y
            for _, y in filter(
                lambda x: x[0] not in failed, enumerate(filteredPatterns)
            )
        ]

    return filteredPatterns