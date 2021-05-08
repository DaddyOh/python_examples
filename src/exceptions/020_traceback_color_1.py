"""
https://www.learnpython.dev/03-intermediate-python/40-exceptions/10-all-about-exceptions/
"""
import traceback
import custom_exceptions as cx
import rich.traceback as rt

def a_function():
    raise cx.MyException(" a message")
"""
I thought that the traceback image from rich would be colorized
See 030_ file 
https://rich.readthedocs.io/en/latest/traceback.html
"""
def main():
    print("Demo basic of exceptions")
    print("a custom exception class")
    c = rt.Console()
    try:
        a_function()
    except cx.MyException as e:
        traceback.print_exc()
        print("=====")
        c.print_exception()
        pass


if __name__ == '__main__':
    main()