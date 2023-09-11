# Function to check if a number is prime
def is_prime(num)
    return false if num <= 1
    return true if num <= 3
  
    return false if num % 2 == 0 || num % 3 == 0
  
    i = 5
    while i * i <= num
      return false if num % i == 0 || num % (i + 2) == 0
      i += 6
    end
  
    true
  end
  
  # Function to find and print prime numbers up to n
  def find_primes_up_to_n(n)
    (2..n).each do |i|
      puts i if is_prime(i)
    end
  end
  
  # Prompt the user for input
  print "Enter a number (n): "
  n = gets.chomp.to_i
  
  if n < 2
    puts "Please enter a valid number greater than or equal to 2."
  else
    puts "Prime numbers up to #{n}:"
    find_primes_up_to_n(n)
  end
  