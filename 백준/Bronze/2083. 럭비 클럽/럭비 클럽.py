arr = []
while len(arr) == 0 or arr[-1] != ['#', '0', '0']:
    arr.append(list(map(str, input().split())))

arr.pop()

for person in arr:
    if int(person[1]) > 17 or int(person[2]) >= 80:
        print(f"{person[0]} Senior")
    else:
        print(f"{person[0]} Junior")