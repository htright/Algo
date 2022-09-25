# https://velog.io/@minji0801/%EC%98%A4%EB%8B%B5%EB%85%B8%ED%8A%B8%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%8C%EC%9E%84-%EB%A7%B5-%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC
from collections import deque
def solution(maps):
    answer = 0

    # 동남서북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

                # 벽이면 무시하기
                if maps[nx][ny] == 0:  continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    # 지나간 길은 maps[nx][ny] = 2 로 만든다. 또한 돌아가는 경우 dfs가 아닌 bfs로 최단거리 조건에
                    # 부합하지 않은 것은 제외되는 것을 알 수 있다.
                    maps[nx][ny] = maps[x][y] + 1 
                    queue.append((nx, ny))    # 재귀

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer    # 상대 팀 진영에 도착할 수 없을 때 -1

# solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) 