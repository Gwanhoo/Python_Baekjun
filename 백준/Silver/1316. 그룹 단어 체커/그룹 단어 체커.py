# 문자열 개수 입력받기
N = int(input())
answer = N
# N번 반복
for _ in range(N):
    alphabet_list = []
    word = input()
    # 단어길이 수 - 1 만큼 순회
    for alphabet in range(len(word)-1):
        # 알파벳 리스트에 현재 인덱스 번호의 알파벳 추가
        alphabet_list.append(word[alphabet])
        # 마지막 알파벳은 현재 단어의 인덱스 번호
        last_alphabet = word[alphabet]
        # 만약 마지막 알파벳과 그 다음 알파벳이 같다면
        if last_alphabet == word[alphabet+1]:
            # 넘어가기
            continue
        # 만약 다르다면
        elif last_alphabet != word[alphabet+1]:
            # 알파벳 리스트에 추가 되었던 알파벳인지 확인
            if word[alphabet+1] in alphabet_list:
                answer -= 1
                break


print(answer)