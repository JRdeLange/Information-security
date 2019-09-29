import math
import fileinput

def modular_pow_recursive(base, exponent, modulus):
    # Check if the modulus is not 1 (otherwise 0 should be returned).
    if (modulus == 1):
        return 0
    # Take the modulus of the base if possible.
    base = base % modulus
    return modular_pow(base, exponent, modulus, 1)

def modular_pow(base, exponent, modulus, result):
    # Calculate the answer using the right-to-left binary method
    if (exponent > 0):
        # Checks if it would have been a 1 or a 0 in binary form.
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = math.floor(exponent / 2)
        base = (base * base) % modulus

        return modular_pow(base, exponent, modulus, result) 
    else:
        # If the exponent is 0, we got the final answer.
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
            print("Please enter valid numbers.")
            continue
        
        print(modular_pow_recursive(numbers[0], numbers[1], numbers[2]))
