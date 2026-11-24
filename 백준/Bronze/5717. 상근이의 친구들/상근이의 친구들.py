while True:
    line = input()
    if line == "0 0":
        break
    M, F = map(int, line.split())
    print(M + F)