#! python3
# INCOMPLETE, needs 8 second timer, and 3 tries per question
import time, random, re

number_of_questions = 10
correct_answers = 0
for i in range(1, 10):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    regex = re.compile(r'^\d+$')
    prompt = 'Question #%s: %s x %s = ' % (i, num1, num2)
    answer = str(input(prompt))
    mo = regex.search(answer)
    if (mo.group() is not None) and (int(mo.group()) == (num1 * num2)):
        correct_answers += 1
        print('Correct!')
    elif mo.group() != (num1 * num2):
        print('Incorrect!')
