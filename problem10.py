# find the sum of all primes below 2 million

# plan:
# a functiong that determines if a number is prime or not
# create a list of all prime below two million
# sum the list of primes

# function that figures out if a number is a prime or not
def isPrime(n):
    count = 0
    for i in range(1, n + 1):
        if (n % i == 0):
            count += 1
            if (count > 2):
                return False
    if (count == 2):
        return True
# print(isPrime(10))

# a function that lists all the prime numeber below 2000000
def primeBelowTwoMillion():
    listOfAllPrime = []
    for i in range(1, 2000001):
        if (isPrime(i) == True):
            listOfAllPrime.append(i)
    return listOfAllPrime

# print(primeBelowTwoMillion())

# a function that sums all the given prime numbers list
primeList = primeBelowTwoMillion()
def sumOfAllPrime(list):
    sum  = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

print(sumOfAllPrime(primeList))
