def series_sum(n):
    sum = 0
    k = 1
    for i in range(n):
        sum+=1/(i+k)
        k+=2
    return f'{sum:.2f}'