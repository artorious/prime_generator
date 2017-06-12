from math import factorial
def primeNumbers(n):
    """(int) -> list 

    Takes a positive number n  
    Returns a list of all prime numbers between 0 and n (inclusive)
    
    >>>primeNumbers(9)
    [1, 2, 3, 5, 7]
    """
    if not isinstance(n, int) or n < 0:
        raise TypeError
    
    return [number for number in range(1, n+1) if (factorial(number -1) + 1) % number == 0]
