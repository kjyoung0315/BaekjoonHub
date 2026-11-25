N = int(input())

problems = [int(input()) for _ in range(N)]

cnt = 0
for problem in problems:
    if problem % 2 != 0:
        cnt += 1

print(cnt)