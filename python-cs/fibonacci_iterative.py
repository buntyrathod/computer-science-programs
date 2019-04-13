# ----------------------------------
# Fibonacci with iterative approach
# ----------------------------------

def fibonacci(num: int) -> int:
    #Special case   
    if(num == 0):
        return 0
    #Intial 
    second_last = 0
    first_last = 1
    for _ in range(1, num):
        second_last, first_last = first_last, second_last + first_last
    return first_last

if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci(50))
