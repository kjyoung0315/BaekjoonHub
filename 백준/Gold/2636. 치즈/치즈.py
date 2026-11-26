from collections import deque
import sys

input = sys.stdin.readline

row, column = map(int, input().split())
cheezes = [list(map(int, input().split())) for _ in range(row)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

hour = 0
last_cheese_count = 0

while True:
    stack = []
    for y in range(row):
        for x in range(column):
            if cheezes[y][x] == 1:
                stack.append([x, y])
    
    if not stack:
        break
        
    last_cheese_count = len(stack)
    
    visited = [[False] * column for _ in range(row)]
    q = deque([(0, 0)])
    visited[0][0] = True
    
    this = []
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < column and 0 <= ny < row and not visited[ny][nx]:
                visited[ny][nx] = True
                if cheezes[ny][nx] == 0:
                    q.append((nx, ny))
                elif cheezes[ny][nx] == 1:
                    this.append([nx, ny])
                    
    this = list(map(list, set(tuple(pos) for pos in this)))

    for x, y in this:
        cheezes[y][x] = 0
        
    hour += 1

print(hour)
print(last_cheese_count)