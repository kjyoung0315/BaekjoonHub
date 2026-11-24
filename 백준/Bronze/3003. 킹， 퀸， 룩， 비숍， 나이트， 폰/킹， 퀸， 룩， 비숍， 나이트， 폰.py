arr = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]
result = []
for i in range(len(arr)):
    result.append(chess[i] - arr[i])

for j in result:
    print(j, end=' ')