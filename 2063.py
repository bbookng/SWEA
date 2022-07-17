N = int(input())

arr = list(map(int, input().split()))

arr.sort()
result = arr[N//2]

print(result)