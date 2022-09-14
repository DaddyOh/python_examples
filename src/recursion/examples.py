def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

# https://realpython.com/fibonacci-sequence-python/#getting-started-with-the-fibonacci-sequence
def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n

    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

def main():
    num = 3
    print("The factorial of", num, "is", factorial(num))

    print()
    print('fib of 15')
    print([fibonacci_of(n) for n in range(15)])

if __name__ == '__main__':
    main()

    