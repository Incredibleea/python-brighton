def factorial(n):
    """Function returning factorial of \'n\'"""
    val = 1
    for i in range(1,n+1):
        val *= i
    return val

def fibonacci(n):
    """Function returning nth element in fibonacci sequence"""
    a = 1
    b = 1
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n+1):
            temp = b
            b += a
            a = temp
        return b