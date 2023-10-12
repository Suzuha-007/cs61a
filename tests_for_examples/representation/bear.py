class Bear:
    #  """A Bear.
    
    
    # >>> oski = Bear()
    # >>> oski
    # Bear()
    # >>> print(oski)
    # a bear
    # >>> print(str(oski))
    # a bear,  str()能直接调用类的方法
    # >>> print(repr(oski))
    # Bear(),   repr()同样能直接调用类的方法
    # >>> print(oski.__repr__())
    # oski，    调用实例的方法
    # >>> print(oski.__str__())
    # oski the bear

    # >>> print(str_(oski))
    # a bear
    # >>> print(repr_(oski))
    # Bear()
    # """
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'oski the bear'

    def __repr__(self):
        return 'Bear()'
    
    def __str__(self):
        return 'a bear'

def repr_(x):
       s = type(x).__repr__(x) #Bear.__repr__(oski)
       if not isinstance(s, str):
              raise TypeError
       return s

def str(x):
    s = type(x).__str__(x)
    if not isinstance(s, str):
        raise TypeError
    return s

        