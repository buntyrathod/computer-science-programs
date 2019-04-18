#--------------------------------------------------------------
# Generating list of fibonacci numbers using python Generator
#--------------------------------------------------------------
from typing import Generator

def fibonacci(num: int) -> Generator[int, None, None]:
    # Special cases
    yield 0 
    if num > 0: yield 1
    
    # Main generation steps
    second_last: int = 0
    first_last: int = 1
    for _ in range(1, num):
        second_last, first_last = first_last, first_last + second_last
        yield first_last

if __name__ == '__main__':
    for i in fibonacci(50):
        print(i)
    