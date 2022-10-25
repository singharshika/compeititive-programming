t = int(input())

def func(x, y, t1, t2, n):
    if (x == 1 and y == 1) or (x == n and y == 1) or (x == 1 and y == n) or (x == n and y == n):
        if x == t1 or y == t2:
            print("YES")
        else:
            print("NO")
        return
    if x%2 and y%2:
        print("NO" if (t1%2 == 0 and t2%2 == 0) else "YES")
    elif x%2 and y%2 == 0:
        print("NO" if (t1%2 == 0 and t2%2) else "YES")
    elif x%2 == 0 and y%2:
        print("NO" if (t1%2 and t2%2 == 0) else "YES")
    else: 
        print("NO" if (t1%2  and t2%2) else "YES")



while t:
    n = int(input())
    a = list(map(int,input().split()))
    t1, t2 = map(int, input().split())
    if (a[0] == a[2] or a[0] == a[4]) and (a[1] == a[3] or a[1] == a[5]):
        func(a[0], a[1], t1, t2, n)
    elif (a[2] == a[0] or a[2] == a[4]) and (a[3] == a[1] or a[3] == a[5]):
        func(a[2], a[3], t1, t2, n)
    else:
        func(a[4], a[5], t1, t2, n)

    t-=1
