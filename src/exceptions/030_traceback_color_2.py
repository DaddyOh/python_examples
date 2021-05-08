"""
https://www.learnpython.dev/03-intermediate-python/40-exceptions/10-all-about-exceptions/

https://rich.readthedocs.io/en/latest/traceback.html
"""
import traceback
import custom_exceptions as cx
import rich.traceback as rt

def a_function():
    raise cx.MyException(" a message")
"""
I thought that the traceback image from rich would be colorized
See 030_ file 
# color is just red - the listing is interesting.
# I'm not sure this is worth doing.

"""
def main():
    rt.install() # this only works with uncaught exceptions
    print("Demo basic of exceptions")
    print("a custom exception class")
    a_function()




if __name__ == '__main__':
    main()