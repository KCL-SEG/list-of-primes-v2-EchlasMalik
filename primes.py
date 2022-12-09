"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes<1):
        raise ValueError("0 and negative numbers not accepted")
    list = []
    number = 0
    prime_number = 2
    is_prime = True

    while number < (number_of_primes):
        for n in range(2,prime_number):
            if(prime_number % n == 0):    #Checks if any number between 2 and itself divide. (Checking for any non-prime numbers)
                is_prime = False
            
            elif is_true == True:
                list.append(prime_number)
                count = count + 1
            
            prime_number = prime_number + 1
    return list
