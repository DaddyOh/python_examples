"""
Can we capture stderr and dtermine what is in the contents

Python logger to console is said to log to stderr

"""

from io import StringIO  # Python 3
import sys

print("A This is being written to stdout")
print("B Out to stderr", file=sys.stderr)
# Create the in-memory "file"
temp_out = StringIO()

# Replace default stdout (terminal) with our stream
sys.stderr = temp_out

print("C This is being written to stdout")
print("D Out to stderr XYZZY", file=sys.stderr)

temp_out.write("Can be written to like normal.\n")

# The original `sys.stdout` is kept in a special
# dunder named `sys.__stdout__`. So you can restore
# the original output stream to the terminal.
sys.stdout = sys.__stdout__

print("Now printing back to terminal")
print("The 'fake' stdout contains: =======")
content_ = temp_out.getvalue()
sys.stdout.write(content_)
print("=============================")

if "XYZZY" in content_:
    print("Success we captured stderr because we can detect 'XYZZY'")
