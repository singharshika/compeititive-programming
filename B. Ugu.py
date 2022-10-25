t = int(input())
while t:
    n = int(input())
    s = input()
    i = 0
    while i < len(s) and s[i] == '0':
        i+=1
    parity = 0
    ans = 0
    while i < len(s):
        if parity:
            if s[i] == '1':
                ans+=1
                parity = ~parity
        else:
            if s[i] == '0':
                ans+=1
                parity = ~parity
        i+=1
    print(ans)
    t-=1
