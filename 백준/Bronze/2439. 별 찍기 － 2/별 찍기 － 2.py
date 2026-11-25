N = int(input())

space = N-1
star = 1
for _ in range(N):
    for _ in range(space):
        print(' ', end='')
    for _ in range(star):
        print('*', end='')
    star += 1
    space -= 1
    print()