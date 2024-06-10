# 함수로 N 입력받기
def hansu(n):
    result = 0
    for i in range(1, n+1):
        num_list = list(map(int, str(i)))
        # i가 100 미만일때는 모두 한수 100 이상일때는 값 비교해야함
        if i < 100:
            result += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            result += 1

    return result

n = int(input())
print(hansu(n))