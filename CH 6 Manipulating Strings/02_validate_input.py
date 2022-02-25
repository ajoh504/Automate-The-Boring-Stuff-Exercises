''' The following code requires the user to input their age and a new password. 
The isdecimal() and isalnum() methods ensure that the user input follows specific
criteria.'''

while True:
  print('Enter your age:')
  age  = input()
  if age.isdecimal():
    break
  print('Please enter a number for your age.')
while True:
  print('Select a new password (letters and numbers only):')
  password = input()
  if password.isalnum():
    break
  print('Passwords can only have letters and numbers.')
