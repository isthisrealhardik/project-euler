# sum of the squares of the first ten natural numbers: 1^2 + 2^2 ... 10^2 = 385
# square of the sum of the first ten natural numbers (1 + 2 + ... + 10) ^ 2 = 3025
# difference 3025 - 385 = 2640

# find the same thing for 'n' natural numbers specified by the user

naturalNum = 100

def sumOfTheSquare(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum

def squareOfTheSum(n):
    power = 0
    for i in range(1, n + 1):
        power += i
    sum = power ** 2
    return sum


def difference(n):
    sumOf = sumOfTheSquare(naturalNum)
    squareOf = squareOfTheSum(naturalNum)
    return squareOf - sumOf

print(difference(naturalNum))

