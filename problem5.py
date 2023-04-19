# 2520 is the smallest divisble number by each from 1 to 10.
# What is the smallest positive number that is divisble by each integrer from 1 to 20?

def smallestPositiveNumber():
    n = 1
    while(True):
        i = 1
        count = 0
        while (i <= 20):
            if (n % i == 0):
                count += 1
            i += 1
        if (count == 20):
            break
        n += 1
    print(n)

print(smallestPositiveNumber())