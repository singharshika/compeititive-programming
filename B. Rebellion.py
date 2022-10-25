t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    l,r = [0,n-1]
    ans = 0
    while l < r:
        while l < r and a[l] == 0:
            l+=1
        while l < r and a[r] ==  1:
            r-=1
        if l < r:
            ans+=1
            l+=1
            r-=1
    print(ans)

    t-=1
