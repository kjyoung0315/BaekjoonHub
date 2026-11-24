arr = []

while len(arr) == 0 or arr[-1] != [0, 0]:
    arr.append(list(map(int, input().split())))

arr.pop()

for judge_arr in arr:
    if judge_arr[0] > judge_arr[1]:
        print("Yes")
    else:
        print("No")