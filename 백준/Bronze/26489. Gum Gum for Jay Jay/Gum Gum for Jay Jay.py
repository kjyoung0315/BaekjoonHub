cnt = 0

while True:
    try:
        gum = input()
        if not gum:  # 빈 줄이 입력되면 반복문 종료
            break
        cnt += 1
    except EOFError:
        break

print(cnt)