# Recursions: Recursive Vs Iterative Approach
# n! = n * n-1 * n-2 * n-3 ...... 1
# n! = n * (n-1)!

def factorial_iterative(n):
    """
       Iterative method
       :param n: Integer
       :return: n * n-1 * n-2 * n-3 ...... 1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


def factorial_recursive(n):
    """
    Recursive method
    :param n: Integer
    :return: n * n-1 * n-2 * n-3 ...... 1
    5 * factorial_recursive(4)
    5 * 4 * factorial_recursive(3)
    5 * 4 * 3 * factorial_recursive(2)
    5 * 4 * 3 * 2 * factorial_recursive(1)
    5 * 4 * 3 * 2 * 1 = 120
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


number = int(input("Enter the number:- "))
# print("factorial using iterative method :- ", factorial_iterative(number))
# print("factorial using Recursive method :- ", factorial_recursive(number))
# print(factorial_recursive.__doc__)

# Quiz


def fibonacci_iterative(n):
    """
    :param n: Integer
    :return: n, n+1, n+(n+1), (n+1)+(n+(n+1)), (n+(n+1))+(n+1)+(n+(n+1)) ......
    """
    list1 = []
    a = 0
    b = 1
    for i in range(n):
        list1.append(a)
        result = a + b
        a = b
        b = result
    return list1


def fibonacci_recursive(n):
    """
    :param n: Integer
    :return: n, n+1, n+(n+1), (n+1)+(n+(n+1)), (n+(n+1))+(n+1)+(n+(n+1)) ......
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print("fibonacci series  using iterative method :- ", fibonacci_iterative(number))
print("fibonacci series  using recursive method :- ", fibonacci_recursive(number))
