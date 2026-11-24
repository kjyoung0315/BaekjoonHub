A = str(input())
result = ""
for i in A:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()

print(result)