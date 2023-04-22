# figoure the a pythag triplet where a + b + c = 1000, and find the product of abc?
#  hint: there only exist one and a < b < c

# a function to figure out if the given three numbers are a pT?
def pT(arr):
    if (arr[2] > arr[1] and arr[1] > arr[0]):
        if (arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2):
            return True
        else:
            return False

# all the possible ways where a + b + c can add upto 1000
def allPossibleVal():
    #  try: a + b = 100
    listOfPossibleVal = []
    tillN = 1000
    a = 1
    while (a <= tillN):
        b = 1
        while (b <= tillN):
            c = 1
            while (c <= tillN):
                if (a + b + c == tillN):
                    listOfPossibleVal.append([a, b, c])
                c += 1
            b += 1
        a += 1
    return listOfPossibleVal

# figure out the product now
arr = allPossibleVal()
def product (arr):
    for i in range(len(arr) - 1):
        if (pT(arr[i]) == True):
            return arr[i][0] * arr[i][1] * arr[i][2]
        
print(product(arr))
