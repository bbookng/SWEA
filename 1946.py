T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    total = ''

    for _ in range(N):
        String, times = input().split()
        total += (String * int(times))

    i = 0
    while i*10 < len(total):
        print(total[i*10: (i+1)*10])
        i += 1