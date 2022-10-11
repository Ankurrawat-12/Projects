# Function Caching In Python
import time
from functools import lru_cache
a = 6


@lru_cache(maxsize=a)
def some_work(n):
    """Some task taking n seconds"""
    # global i
    # i += 1
    # print(i)
    time.sleep(n)
    return n


# i = 1
if __name__ == '__main__':
    print("Now Running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print(f"Done.... Calling again")
    input()
    some_work(3)
    print(f"Called again")
    some_work(3)
    print(f"Called again")
    some_work(3)
    print(f"Called again")
    # g = some_work(5)
    # print(f"{g} Done.... Calling again")
    # g = some_work(4)
    # print(f"{g} Called again")
    # g = some_work(3)
    # print(f"{g} Done.... Calling again")
    # g = some_work(2)
    # print(f"{g} Called again")
    # g = some_work(3)
    # print(f"{g} Done.... Calling again")
    # g = some_work(2)
    # print(f"{g} Called again")
