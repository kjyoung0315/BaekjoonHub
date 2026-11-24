arr = []

while len(arr) == 0 or arr[-1] != 0:
    arr.append(int(input()))

arr.pop()

for max_row in arr:
    print(int(max_row*(max_row+1)/2))