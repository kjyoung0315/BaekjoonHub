from collections import deque

M, N, H = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
dh = (-1, 1)
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

day = 0

queue = deque()

for floor in range(H):
    for y in range(len(graph[floor])):
        for x in range(len(graph[floor][y])):
            if graph[floor][y][x] == 1:
                queue.append([x, y, floor])

for loc in queue:
    visited[loc[2]][loc[1]][loc[0]] = 1

while queue:
    x, y, h = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < M) and (0 <= ny < N) and visited[h][ny][nx] == 0 and graph[h][ny][nx] == 0:
            visited[h][ny][nx] = visited[h][y][x] + 1
            graph[h][ny][nx] = 1
            queue.append([nx, ny, h])
    for j in range(2):
        nh = h + dh[j]
        if (0 <= nh < H) and visited[nh][y][x] == 0 and graph[nh][y][x] == 0:
            visited[nh][y][x] = visited[h][y][x] + 1
            graph[nh][y][x] = 1
            queue.append([x, y, nh])

result = 0
max_result = 0
for floor in range(H):
    for y in range(len(graph[floor])):
        layer_max = max(visited[floor][y])
        if layer_max > max_result:
            max_result = layer_max
        for x in range(len(graph[floor][y])):
            if graph[floor][y][x] == 0:
                result = -1

if result == -1:
    print(result)
else:
    print(max_result-1)