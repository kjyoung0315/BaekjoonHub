row = int(input())
star_len = int(input())
stars = ""
for _ in range(star_len):
    stars += "*"
for _ in range(row):
    print(stars)