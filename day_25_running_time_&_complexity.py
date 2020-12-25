def result(number):
    if number == 1:
        return "Not prime"

    if number == 2:
        return "Prime"
    
    if number % 2 == 0:
        return "Not prime"
    # Now we know that our number is not even,
    # sqroot plus 1, can be the one of the dividers
    for i in range(3, int(number**(0.5))+1, 2):
        print(i)
        if number % i == 0:
            return "Not prime"
    return "Prime"

n = int(input())

for i in range(n):
    print(result(int(input()))) 