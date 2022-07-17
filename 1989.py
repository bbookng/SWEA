T = int(input())

for tc in range(1, T + 1):
    string = input().rstrip()
    result = 0

    if string == string[::-1]:
        result = 1
    print(f'#{tc} {result}')