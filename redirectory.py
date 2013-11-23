import sys

def f():
    if sys.version_info > (2, 6) and sys.version_info < (2, 7):
        a()
    if sys.version_info > (2, 7) and sys.version_info < (3, 0):
        b()
    if sys.version_info > (3, 3) and sys.version_info < (4, 0):
        c()
def a():
    print("Here I am in `a`")

def b():
    print("Here I am in `b`")
    print("Here I am in `b`")
    print("Here I am in `b`")

def c():
    print("Here I am in `c`")
    print("Here I am in `c`")
    print("Here I am in `c`")
    print("Here I am in `c`")
    print("Here I am in `c`")
