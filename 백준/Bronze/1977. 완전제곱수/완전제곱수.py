import math

# M과 N 입력 받기
M = int(input())
N = int(input())

result = []
# 반복문 for i in range(M, N+1)
for i in range(M, N+1):
    sqrt_i = math.isqrt(i)
    # i를 루트 씌워서 자연수가 나오면 리스트에 담기
    if sqrt_i * sqrt_i == i:
        result.append(i)

# 리스트가 비어있으면 -1 출력, 그렇지 않으면 합과 최소값 출력
if len(result) == 0:
    print(-1)
else:
    print(sum(result))   # 합계 출력
    print(result[0])     # 최소값 출력


