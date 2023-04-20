# the first six prime numbers are 2, 3, 5, 7, 11 and 13. 
# what is the 10,001st prime number?

# Check if a number is a prime or not
def checkPrime(n):
    count = 0
    for i in range(1, n + 1):
        if (n % i != 0):
            count += 1
    # print(count)
    if (count == n - 2):
        return True
    else:
        return False

# figure out the 10,001st prime?
def nthPrime():
    n = 1
    listOfAllPrimeTillnTh = []
    while True:
        if (len(listOfAllPrimeTillnTh) == 10001):
            return listOfAllPrimeTillnTh[len(listOfAllPrimeTillnTh) - 1]
        else:
            if (checkPrime(n) == True):
                listOfAllPrimeTillnTh.append(n)
        n += 1

print(nthPrime())

