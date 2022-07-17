T = int(input())

for tc in range(1,T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] # matrix 수 배열 input하는 방법

    total = 0
    count = 0

    for i in range(N):

        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0 or j == N-1:
                if count == K:
                    total += 1
                count = 0


    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            if arr[j][i] == 0 or j == N-1:
                if count == K:
                    total += 1
                count = 0

    print("#{} {}".format(tc, total))

