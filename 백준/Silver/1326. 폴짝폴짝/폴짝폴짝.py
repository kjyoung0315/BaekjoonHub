from collections import deque


N = int(input())
arr = list(map(int, input().split()))
start, goal = map(int, input().split())
start -= 1
goal -= 1

jumps = [-1 for _ in range(N)]

queue = deque()
jumps[start] = 0
queue.append(start)

while queue and jumps[goal] == -1:  # goal에 도달할 때까지 탐색
    now = queue.popleft()
    jump = arr[now]  # 현재 징검다리에 적힌 수 (기존 코드에선 변수명이 겹치지 않게 수정)

    # 1. 오른쪽으로 이동
    next_pos = now + jump
    while next_pos < N:
        if jumps[next_pos] == -1:
            jumps[next_pos] = jumps[now] + 1
            queue.append(next_pos)
        next_pos += jump

    # 2. 왼쪽으로 이동
    next_pos = now - jump
    while next_pos >= 0:
        if jumps[next_pos] == -1:
            jumps[next_pos] = jumps[now] + 1
            queue.append(next_pos)
        next_pos -= jump

print(jumps[goal])