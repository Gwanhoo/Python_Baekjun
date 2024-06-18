

# 0. 입력 및 그래프와 방문 정보 초기화
N = int(input())
M = int(input())
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

# dfs 구현

def dfs(idx):
    global visited, graph, answer
    visited[idx] = True
    answer += 1
    
    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)
        
# 1. graph 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# 2. 재귀함수 호출

dfs(1)

# 3. 출력

print(answer - 1)