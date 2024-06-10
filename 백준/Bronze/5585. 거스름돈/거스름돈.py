# 지불할 돈 입력
money = 1000 - int(input())

# 횟수 설정
count = 0

# 동전 종류들
coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    # 몫은 카운트에 +
    count += money // coin
    # 나머지는 money 변수에 저장
    money %= coin

print(count)