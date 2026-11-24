start_loc = input().split()

deltas = {
    'R': (1, 0),
    'L': (-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1)
}

def check_bounds(x, y):
    return  0 <= x < 8 and 0 <= y < 8

king = [ord(start_loc[0][0]) - ord('A'), int(start_loc[0][1]) - 1]
stone = [ord(start_loc[1][0]) - ord('A'), int(start_loc[1][1]) - 1]
moves = int(start_loc[2])

for _ in range(moves):
    move = input()

    delta = deltas[move]

    next_king_x = king[0] + delta[0]
    next_king_y = king[1] + delta[1]

    if not check_bounds(next_king_x, next_king_y):
        continue


    if not (next_king_x == stone[0] and next_king_y == stone[1]):
        king[0] = next_king_x
        king[1] = next_king_y
        continue

    next_stone_x = stone[0] + delta[0]
    next_stone_y = stone[1] + delta[1]

    if not check_bounds(next_stone_x, next_stone_y):
        continue

    king[0] = next_king_x
    king[1] = next_king_y
    stone[0] = next_stone_x
    stone[1] = next_stone_y

print(f"{chr(king[0] + 65)}{king[1]+1}")
print(f"{chr(stone[0] + 65)}{stone[1]+1}")