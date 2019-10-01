import math
import fileinput

def print_generators_for_prime(prime):
    # Algorithm made more or less literally following the exercise description
    prime_factors = compute_prime_factors(prime - 1) 
    generators = []
    for i in range(2, prime - 1):
        generator = True
        for prime_factor in prime_factors:
            exponent = (prime - 1) / prime_factor
            if modular_pow_recursive(i, exponent, prime) == 1:
                generator = False
        if generator:
            generators.append(i)
    return generators

def compute_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Program from exercise 11.
def modular_pow_recursive(base, exponent, modulus):
    if modulus == 1:
        return 0
    base = base % modulus
    return modular_pow(base, exponent, modulus, 1)

# Program from exercise 11.
def modular_pow(base, exponent, modulus, result):
    if exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = math.floor(exponent / 2)
        base = (base * base) % modulus

        return modular_pow(base, exponent, modulus, result)
    else:
        return result
        
if __name__ == '__main__':
    for line in fileinput.input():
        # Remove trainling newline
        line.rstrip()

        numbers = line.split(" ")
        try:
            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])
        except ValueError:
            print("Please enter a valid number.")
            print("If multiple numbers are entered, only the first one will be used.")
            continue
        
        print(print_generators_for_prime(numbers[0]))
