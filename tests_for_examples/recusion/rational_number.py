def rational(n, d):
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    return x('n')

def denom(x):
    return x('d')

# x = rational(3, 7)
# numer(x)
# >>> x
# function
# >>> numer(x)
# 3
# >>> denom(x)
# 7