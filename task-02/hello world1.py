n = int(input("Enter a number: "))
primes = []
for num in range(2, n + 1):
    if all(num % i != 0 for i in range(2, num)):
        primes.append(num)
print("The list of primes are:", primes)