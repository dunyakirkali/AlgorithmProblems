print((lambda _, a: abs(sum(a[:len(a)//2]) - sum(a[len(a)//2:])))(input(), [int(x) for x in input().split()]))