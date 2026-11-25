N = int(input())

year = 2024
month = 8 + 7*(N-1)
if month%12 != 0:
    year += month//12
    month = month%12
else:
    year += month // 12 - 1
    month = 12
print(year, month)