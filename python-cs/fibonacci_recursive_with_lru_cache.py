
# Fibonacci with lru_cache to store intermediate results of the fibonacci computation,
# so that we don't need to re-compute them multiple times, resulting into better performance

from functools import lru_cache

# Stores the result of the function, maxsize=None indicates there is no limit on 
# how many of the most recent calls of the function should be cached
@lru_cache(maxsize=None)
def fibonacci(num: int) -> int:
    if num < 2:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)

if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci(50))
