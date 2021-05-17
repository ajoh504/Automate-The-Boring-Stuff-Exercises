# def spam(divideBy):
#    return 42 / divideBy
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# the above code returns an error when trying
# to divide a number by zero. This is called the
# ZeroDivisionError
# the try and except statements can be used to make
# sure your program does not crash due to an error

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divideBy):
    return 42 / divideBy

# note the following code contains an error. The print functions are
# written inside the try block. When the program hits
# the except clause, it does not return to the try block
# it skips everything after the except clause and the
# program ends, so the final print statement --> print(spam(1))
# will never execute.

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
