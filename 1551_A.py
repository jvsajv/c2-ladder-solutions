# https://codeforces.com/problemset/problem/1551/A

t = int(input())

for i in range(t):
    n = int(input())
    c1 = int(n/3)
    c2 = int((n-c1)/2)
    if c1+(c2*2) < n:
        c1+=1
    print(c1, c2)