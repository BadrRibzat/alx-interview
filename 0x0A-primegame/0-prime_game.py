def isWinner(x, nums):
    def sieve(n):
        """ Return a list of primes up to n """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = []
        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes
    
    def prime_game(n):
        """ Return the winner of the game for a given n """
        primes = sieve(n)
        if not primes:
            return "Ben"
        
        turns = 0
        remaining = [True] * (n + 1)
        
        for prime in primes:
            if remaining[prime]:
                turns += 1
                for multiple in range(prime, n + 1, prime):
                    remaining[multiple] = False
        
        return "Maria" if turns % 2 != 0 else "Ben"

    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

