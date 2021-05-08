"""
https://www.learnpython.dev/03-intermediate-python/40-exceptions/10-all-about-exceptions/
"""

import custom_exceptions as cx

def a_function():
    raise cx.MyException(" a message")

def main():
    print("Demo basic of exceptions")
    print("a custom exception class")
    a_function()
if __name__ == '__main__':
    main()