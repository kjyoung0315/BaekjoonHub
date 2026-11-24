T = int(input())

for test_case in range(1, T+1):
    word = input()
    print(f"{word[0]}{word[len(word)-1]}")