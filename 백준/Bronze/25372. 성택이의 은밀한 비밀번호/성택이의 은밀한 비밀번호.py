T = int(input())

for test_case in range(1, T+1):
    password = input()
    if 6 <= len(password) <=9:
        print("yes")
    else:
        print("no")