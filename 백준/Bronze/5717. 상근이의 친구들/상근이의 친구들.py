arr = []

while len(arr) == 0 or arr[-1] != [0, 0]:
    arr.append(list(map(int, input().split())))

arr.pop()
    
for i in arr:
    print(sum(i))