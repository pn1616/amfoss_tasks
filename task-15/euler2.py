t = int(input())
for i in range(t):
    N = int(input())
    a, b = 1, 2
    sum = 0
    while a <= N:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    print(sum)                 
        
