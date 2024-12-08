### What are **Mathematical Algorithms**?
Mathematical algorithms solve mathematical problems, such as finding factors, calculating powers, or identifying prime numbers. They are fundamental in computer science and number theory.

---

### 1. **Euclid’s Algorithm**
   - **How it works**:
     - Euclid’s Algorithm is used to find the greatest common divisor (GCD) of two integers. It is based on the principle that the GCD of two numbers also divides their difference.
     - The algorithm repeatedly replaces the larger number with the remainder of dividing the larger number by the smaller number until one of the numbers becomes zero. The non-zero number at this point is the GCD.

   - **Example Explanation**:
     - To find the GCD of 48 and 18:
       - \( 48 \mod 18 = 12 \)
       - \( 18 \mod 12 = 6 \)
       - \( 12 \mod 6 = 0 \)
       - Thus, GCD(48, 18) = 6.

   **Python Code**:
   ```python
   def gcd(a, b):
       while b != 0:
           a, b = b, a % b
       return a

   # Example usage
   num1 = 48
   num2 = 18
   result = gcd(num1, num2)
   print(f"The GCD of {num1} and {num2} is: {result}")
   ```

---

### 2. **Sieve of Eratosthenes**
   - **How it works**:
     - The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a specified integer \( n \). It works by iteratively marking the multiples of each prime starting from 2.
     - The algorithm maintains a list of boolean values representing the primality of numbers. Initially, all numbers are considered prime, and multiples of each prime are marked as non-prime.

   - **Example Explanation**:
     - To find all prime numbers up to 30:
       - Start with a list from 2 to 30.
       - Mark the multiples of each number starting from 2 as non-prime. After processing, the unmarked numbers will be primes.

   **Python Code**:
   ```python
   def sieve_of_eratosthenes(n):
       is_prime = [True] * (n + 1)
       p = 2
       while (p * p <= n):
           if is_prime[p]:
               for i in range(p * p, n + 1, p):
                   is_prime[i] = False
           p += 1
       prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
       return prime_numbers

   # Example usage
   n = 30
   primes = sieve_of_eratosthenes(n)
   print(f"Prime numbers up to {n} are: {primes}")
   ```

---

### 3. **Fast Exponentiation**
   - **How it works**:
     - Fast exponentiation, also known as exponentiation by squaring, is an efficient method to compute \( x^n \) (x raised to the power n) in logarithmic time. It reduces the number of multiplications needed by breaking down the exponentiation process.
     - If \( n \) is even, \( x^n = (x^{n/2})^2 \). If \( n \) is odd, \( x^n = x \cdot x^{n-1} \). This allows for fewer calculations by leveraging previously calculated powers.

   - **Example Explanation**:
     - To compute \( 2^{10} \):
       - \( 2^{10} = (2^5)^2 \)
       - \( 2^5 = 2 \cdot (2^2)^2 \)
       - \( 2^2 = 4 \)
       - The process requires fewer multiplications compared to naïvely multiplying 2 ten times.

   **Python Code**:
   ```python
   def fast_exponentiation(x, n):
       if n == 0:
           return 1
       elif n % 2 == 0:
           half = fast_exponentiation(x, n // 2)
           return half * half
       else:
           return x * fast_exponentiation(x, n - 1)

   # Example usage
   base = 2
   exponent = 10
   result = fast_exponentiation(base, exponent)
   print(f"{base}^{exponent} = {result}")
   ```

---

### Summary of **Mathematical Algorithms**:
1. **Euclid’s Algorithm**: Efficiently finds the GCD of two integers using repeated division.
2. **Sieve of Eratosthenes**: Quickly finds all prime numbers up to a specified integer by marking multiples of each prime.
3. **Fast Exponentiation**: Calculates powers in logarithmic time using a divide-and-conquer approach to reduce the number of multiplications.

These algorithms are fundamental in number theory, cryptography, and various computational applications. Understanding them enhances your problem-solving skills in mathematics and computer science.