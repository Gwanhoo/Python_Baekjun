# kg 입력 받기
kg = int(input())

count = 0
# kg 값이 5로 나누어떨어질때까지 3으로 뺀 후에 5로 나눈다

while kg >= 0:
    if kg % 5 == 0:
        count += int(kg // 5)
        print(count)
        break
    kg -= 3
    count += 1
else:
    print(-1)

