t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    l = dict()
    for i in range(n):
        l[a[i]] = i+1
    for i in range(n, 0,-1):
        print(l[i], end = ' ')
    print()
    t-=1
