N = int(input())

for test_case in range(N):
    A, B, X = map(int, input().split())
    result = A*(X-1)+B
    print(result)