A, B = map(int, input().split())
if A > B:
    result = '>'
elif A < B:
    result = '<'
else:
    result = '=='
print(result)