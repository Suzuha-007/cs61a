def split(n):
    return n //10, n % 10

def luhn_sum(n):
    ## basic case
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        ## to double all_but_last' last bit due to that last is odd
        return luhn_sum_double(all_but_last) + last
    
def luhn_sum_double(n):
    all_but_last, last = split(n)
    last *= 2
    if last >= 10:
        last = last % 10 + last // 10

    if n < 10:
        return last


    
    else:
        return luhn_sum(all_but_last) + last
