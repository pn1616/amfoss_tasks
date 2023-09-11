#include <stdio.h>

int main() {
    int n;
    printf("Enter a number (n): ");
    scanf("%d", &n);

    if (n < 2) {
        printf("There are no prime numbers less than 2.\n");
    } else {
        printf("Prime numbers up to %d are: ", n);

        for (int num = 2; num <= n; num++) {
            int is_prime = 1; // Assume num is prime initially

            for (int i = 2; i * i <= num; i++) {
                if (num % i == 0) {
                    is_prime = 0; // num is not prime
                    break;
                }
            }

            if (is_prime) {
                printf("%d ", num);
            }
        }
        printf("\n");
    }

    return 0;
}
