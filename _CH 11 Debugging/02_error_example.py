# a call stack example

def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')
spam()

# C:\CS\Python\python.exe "C:/CS/Python/PyCode/ATBS/CH 11/error_example.py"
# Traceback (most recent call last):
#   File "C:\CS\Python\PyCode\ATBS\CH 11\error_example.py", line 7, in <module>
#     spam()
#   File "C:\CS\Python\PyCode\ATBS\CH 11\error_example.py", line 4, in spam
#     bacon()
#   File "C:\CS\Python\PyCode\ATBS\CH 11\error_example.py", line 6, in bacon
#     raise Exception('This is the error message.')
# Exception: This is the error message.
#
# Process finished with exit code 1
