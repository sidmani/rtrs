class Symbol:
    def __init__(self, name):
        self.name = name

    def __eq__(self, o):
        return isinstance(o, Symbol) and self.name == o.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
    
    def __hash__(self):
        return hash("Symbol_" + self.name)


class Variable:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash("Variable_" + self.name)