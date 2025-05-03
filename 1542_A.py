# https://codeforces.com/problemset/problem/1542/A

t = int(input())
qntOdd = 0
qntEven = 0
for i in range(t):
    n = int(input())
    nums = input().split()
    for j in range(2*n):
        if int(nums[j])%2 == 0:
            qntEven+=1
        else:
            qntOdd+=1
    if(qntOdd == qntEven):
        print("Yes")
    else:   
        print("No")
    qntEven = 0 
    qntOdd = 0
         
    