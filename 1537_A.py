# https://codeforces.com/problemset/problem/1537/A
t = int(input())

for i in range(t):
    n = int(input())
    nums = input().split()
    sum = 0
    newSum = 0

    for i in range(n):
        sum += int(nums[i])
    
    if(sum/n == 1):
        print(newSum)
    else:
        if(n > sum):
            newSum = 1
        else:
            newSum = sum - n
        print(newSum)
