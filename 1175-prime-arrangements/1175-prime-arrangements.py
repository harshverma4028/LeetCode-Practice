class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        
        MOD = 10**9 + 7
        prime_count = 0

        for num in range(2, n + 1):
            is_prime = True

            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_count += 1

        def factorial(x):
            res = 1
            for i in range(2, x + 1):
                res = (res * i) % MOD
            return res

        prime_ways = factorial(prime_count)
        non_prime_ways = factorial(n - prime_count)

        return (prime_ways * non_prime_ways) % MOD