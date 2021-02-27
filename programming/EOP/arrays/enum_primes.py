# Write a program that takes an integer argument and returns all the primes between 1 and that integer.

def generate_primes(n):

    primes = []

    is_prime = [False, False] + [True]*(n-1)

    for p in range(2, n+2):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n+1, p):
                is_prime[i] = False
    
    return primes