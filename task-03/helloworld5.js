// Function to check if a number is prime
function isPrime(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
  
    if (num % 2 === 0 || num % 3 === 0) return false;
  
    for (let i = 5; i * i <= num; i += 6) {
      if (num % i === 0 || num % (i + 2) === 0) return false;
    }
  
    return true;
  }
  
  // Function to find and print prime numbers up to n
  function findPrimesUpToN(n) {
    for (let i = 2; i <= n; i++) {
      if (isPrime(i)) {
        console.log(i);
      }
    }
  }
  
  // Prompt the user for input
  const n = parseInt(prompt("Enter a number (n):"));
  
  if (isNaN(n) || n < 2) {
    console.log("Please enter a valid number greater than or equal to 2.");
  } else {
    console.log(`Prime numbers up to ${n}:`);
    findPrimesUpToN(n);
  }
  