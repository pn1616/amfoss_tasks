import math

def largestprimefactor(N):
    while N % 2 == 0:
        N //= 2


    maxprime = 2


    for i in range(3, int(math.sqrt(N)) + 1, 2):
        while N % i == 0:
            maxprime = i
            N //= i

    
    if N > 2:
        maxprime = N

    return maxprime


T = int(input())

for _ in range(T):
    N = int(input())
    result = largestprimefactor(N)
    print(result)

