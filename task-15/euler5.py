import math

t = int(input())
for _ in range(t):
    def smallestmultiple(n):
        lcm = 1
        for i in range(2, n + 1):
            lcm = (lcm * i) // math.gcd(lcm, i)
        return lcm

    N = int(input())

    if N < 1:
        print("error")
    else:
        result = smallestmultiple(N)
        print(result)

