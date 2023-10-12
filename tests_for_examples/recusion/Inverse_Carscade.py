def Inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)

        g(n)

shrink = lambda n: f_then_g(print, shrink, n // 10)
grow = lambda n: f_then_g(grow, print , n // 10)


#   grow(123), print 123, shrink(123)
# 
   # ->grow(12), which return none,thenprint 12
    #     ->grow(1),which return none,then print 1
#  const char[1, 2, 3]
