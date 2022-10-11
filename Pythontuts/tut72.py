# Generators In Python

"""
Iterable -> __iter__() or __getitem__()
Iterator -> __next__()
Iteration ->

yield is a keyword in Python that is used to return from a function without
destroying the states of its local variable and when the function is called,
the execution starts from the last yield statement. Any function that contains
a yield keyword is termed as generator. Hence, yield is what makes a generator
"""

"""
def gen(n):
    for i in range(n):
        yield i


g = gen(100)
print(type(g))
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

h = "harry"
# h = 1344  # int is not iterable

ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# print(h[0])
# for c in h:
#     print(c)

"""


def factorial(n):
    result = 1
    for i in range(n):
        result *= n
        n -= 1
    yield result


def fibonacci(n):
    result = 0
    a = 0
    b = 1
    for i in range(n):
        result += a
        a = b
        b = result
        yield result


# fac = factorial(5)
# print(fac.__next__())

fib = fibonacci(12)
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
