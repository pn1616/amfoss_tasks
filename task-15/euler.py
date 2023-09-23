def sumofmultiples(k, n):
    p = (n - 1) // k
    return k * (p * (p + 1)) // 2

def sumofmultiplesbelown(N):
    return sumofmultiples(3, N) + sumofmultiples(5, N) - sumofmultiples(15, N)

T = int(input())

for i in range(T):
    N = int(input())
    result = sumofmultiplesbelown(N)
    print(result)
