# This function demonstrates the Collatz sequence in mathematics.
# The function receives a number. If the number is even, it
# returns that number divided by two. If odd, returns that number * 3 and + 1
# The function uses 'try' and 'except' statements to account for
# a non-integer argument. Since the Collatz sequence always evaluates to 1
# no matter the argument, the program will terminate when the number reaches 1
# or if the input is not an integer

def collatz(number): # function receives an argument, number
    try:
        if int(number) % 2 == 0: # checks to see if even number
            print(int(number) // 2)
            return (int(number) // 2)
        elif int(number) % 2 == 1: # checks to see if odd number
            print(3 * int(number) + 1)
            return (3 * int(number) + 1)
    except (ValueError, TypeError): # except statement for non-integer
        print('Value must be an integer')
        
while True:
  num = collatz(input()) # user inputs number into collatz, then stored in num
  while True: # while loop calls Collatz function until the number reaches 1
      if num == 1:
          break
      elif num == None: #if argument is not an integer, collatz returns None. 
          break
      num = collatz(num) # num is passed into collatz
