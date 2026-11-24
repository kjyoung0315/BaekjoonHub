N = int(input())
arr = list(map(int, input().split()))
v = int(input())
cnt_v = 0
for i in arr:
    if i == v:
        cnt_v += 1
print(cnt_v)