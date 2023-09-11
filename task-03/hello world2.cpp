#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    // Iterate through all the numbers from 2 to n
    for (int i = 2; i <= n; i++) {
        bool isPrime = true;

        // Check if the number is divisible by any number from 2 to its square root
        for (int j = 2; j <= sqrt(i); j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }

        // If the number is prime, print it out
        if (isPrime) {
            cout << i << " ";
        }
    }

    cout << endl;

    return 0;
}