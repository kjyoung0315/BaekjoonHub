N = int(input())

result = 1
if N == 0:
    pass
else:
    while N != 0:
        result = result * N
        N -= 1
print(result)