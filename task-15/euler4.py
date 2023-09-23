def palindrome(n):
    return str(n) == str(n)[::-1]

def largestpalindromeproduct(N):
    largestpalindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < N and palindrome(product) and product > largestpalindrome:
                largestpalindrome = product
            if product <= largestpalindrome:
                break
    return largestpalindrome

T = int(input())

for k in range(T):
    N = int(input())
    result = largestpalindromeproduct(N)
    print(result)

