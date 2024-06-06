from itertools import combinations

# 카드 갯수, 지정 숫자 입력
card_num, target_num = map(int, input().split())
# 카드 리스트들 입력
card_list = list(map(int, input().split()))
# 출력값 변수
biggest_num = 0

# (리스트, 원소의 갯수)뽑기
for cards in combinations(card_list, 3):
    # temp_sum에 뽑은 카드들의 합 저장 
    temp_sum = sum(cards)
    # 초기 변수 0 < 뽑은 카드들의 합 <= 지정 숫자면 
    # 타겟에 가까운 수는 biggest_num이다 
    if biggest_num < temp_sum <= target_num:
        biggest_num = temp_sum

print(biggest_num)

