def isWinner(x, nums):
    """Function that determine who has won the most rounds of the prime game."""
    mariaWinsCount = 0
    benWinsCount = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurn = True

        while True:
            if not primesSet:
                if isMariaTurn:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]
            primesSet = [p for p in primesSet if p in roundsSet]

            isMariaTurn = not isMariaTurn

    if mariaWinsCount > benWinsCount:
        return "Maria"
    if benWinsCount > mariaWinsCount:
        return "Ben"
    return None


def is_prime(n):
    """Returning True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returning a list of prime numbers between start and end 'inclusive'."""
    return [n for n in range(start, end + 1) if is_prime(n)]


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

