# this exercise shows that when you call a function, Python
# always returns to the previous line of code where a function
# was first called, even if the function is within another function


def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')
a()
