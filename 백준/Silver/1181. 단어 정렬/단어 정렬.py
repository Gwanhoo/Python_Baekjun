# 단어개수 입력 받기
N = int(input())

word_list = []
# 단어 입력받기
# N번 입력받기
# 반복문
for _ in range(N):
    word = input().strip()
    word_list.append(word)
    # 중복된 단어 set() 사용해서 제거

word_list = list(set(word_list))

# 정렬
ans = sorted(word_list, key=lambda x: (len(x), x))

for answer in ans:
    print(answer)


