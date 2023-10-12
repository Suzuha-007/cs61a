# similar to dfs
def cout_partion(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    
    with_m = cout_partion(n - m, m)
    without_m = cout_partion(n, m - 1)

    return with_m + without_m