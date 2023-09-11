package main

import (
	"fmt"
)

// Function to check if a number is prime
func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	if num <= 3 {
		return true
	}
	if num%2 == 0 || num%3 == 0 {
		return false
	}
	for i := 5; i*i <= num; i += 6 {
		if num%i == 0 || num%(i+2) == 0 {
			return false
		}
	}
	return true
}

// Function to find and print prime numbers up to n
func findPrimesUpToN(n int) {
	for i := 2; i <= n; i++ {
		if isPrime(i) {
			fmt.Println(i)
		}
	}
}

func main() {
	var n int
	fmt.Print("Enter a number (n): ")
	_, err := fmt.Scanf("%d", &n)

	if err != nil || n < 2 {
		fmt.Println("Please enter a valid number greater than or equal to 2.")
	} else {
		fmt.Printf("Prime numbers up to %d:\n", n)
		findPrimesUpToN(n)
	}
}
