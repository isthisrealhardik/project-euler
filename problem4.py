# Largest Palindromic Number from a prodct of two three digit number. 

# create a function that generates the product of all three digit number 
# create a function that returns if the number is palondromic or not
# create a function that takes a list and returns the largest number from the list

### Check if a number is palindromic or not?
# create a function which takes a number
# and breaks that number into a list of numbers
# check if the first and last digit of a number, 
# if yes, move to the next
# do that till the both side reaches the same index

def palOrNot(n):
    if (n < 10):
        return False
    else:
        # turn n into a list of individual things
        list = []

        # process of turning 'n' into a list
        for i in range(len(str(n))):
            list.append(str(n)[i])

        # comparing the current and last ele, if same move on or if not break
        ok = 0
        for i in range(len(list)):
            if (list[i] != list[len(list) - (i + 1)]):
                break
            else:
                ok += 1

        # if 'ok' is same as 'list length', then the number is palindrome
        if (ok == len(list)):
            return True
        else:
            return False
        

# print(palOrNot(906609))

### Generate all the product of two three digit numbers and append the palondromic numebrs to a list


def genAndAppend():
    palList = []
    x1 = 1
    x2 = 1
    
    while (x1 <= 999):
        while (x2 <= 999):
            prod = x1 * x2
            # palList.append(prod)
            if (palOrNot(prod) == True):
                palList.append(prod)
            x2 += 1
        x1 += 1

        x2 = 1
    return palList

palindromicList = genAndAppend()
# if 906609 in palindromicList:
#     print(True)
# else:
#     print(False) 
# print(palindromicList)


# print(palindromicList)

### Find the largest palindromic number from the palindromic list

largest = 0

for i in range(len(palindromicList) - 1):
    if (palindromicList[i] > largest):
        largest = palindromicList[i]

print(largest)