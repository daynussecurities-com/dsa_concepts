import sys
sys.set_int_max_str_digits(0)
class Solution:
    def is_prime(self, n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int):
        if n <= 1:
            return 0
        count = 0
        for i in range(2, n):
            if self.is_prime(i):
                count += 1
        return count


obj = Solution()
print(obj.countPrimes(10))


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        p = 2

        while p * p < n:
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        return sum(prime)