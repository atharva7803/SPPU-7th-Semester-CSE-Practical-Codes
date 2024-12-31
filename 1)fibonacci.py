
def fibIter(n):
    if n < 0:
        return -1,1
    if n == 0 or n == 1:
        return n,1
    
    steps = 0
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        steps += 1
    
    return c, steps 


def fibRec(n):
    if n < 0:
        return -1,1
    if n == 0 or n == 1:
        return n,1
    
    fib1, steps1 = fibRec(n-1)
    fib2, steps2 = fibRec(n-2)
    
    return fib1 + fib2, steps1 + steps2 + 1


def main():
    
    n = int(input("Enter n to calculate Fibonacci number: "))
    
    # Iterative
    print("Using Iterative approach: ", fibIter(n)[0])
    print("Number of steps: ", fibIter(n)[1])
    
    # Recursive
    print("Using Recursive approach: ", fibRec(n)[0])
    print("Number of steps: ", fibRec(n)[1])



if __name__ == "__main__":
    main()








