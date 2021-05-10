# An if statement that checks age, name, etc, but with a bug.
# The age of 3000 evaluates to 'grannie' instead of 'vampire'
# The purpuse of this exercise is to show how an if statement
# might end earlier than intended.

name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
