keys = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

arr = []
while len(arr) == 0 or arr[-1] != '#':
    arr.append(input())

arr.pop()
for sent in arr:
    cnt = 0
    for i in sent:
        if i in keys:
            cnt += 1
    print(cnt)