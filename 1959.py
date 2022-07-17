T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    answer = -199999
    for i in range(len(arr2) - len(arr1) + 1):
        tmp = 0
        for j in range(len(arr1)):
            tmp += (arr1[j] * arr2[j + i])
        if answer < tmp:
            answer = tmp
    print(f'#{tc} {answer}')