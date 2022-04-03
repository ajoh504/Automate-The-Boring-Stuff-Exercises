#! python3
# Make your own multiplication quiz
# INCOMPLETE, needs 8 second timer
import time, random, re

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    # Pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    # regex forces answer to be a digit
    regex = re.compile(r'^\d+$') 
    prompt = 'Question #%s: %s x %s = ' % (question_number, num1, num2)
    # 3 tries per question
    for attempt in range(0, 3): 
        answer = str(input(prompt))
        mo = regex.search(answer)
        if mo == None:
            print('Incorrect')
            # if final try is incorrect, print 'out of tries'
            if attempt == 2:
                print('Out of tries!')
            continue
        elif int(mo.group()) != (num1 * num2):
            print('Incorrect!')
            # if final try is incorrect, print 'out of tries'
            if attempt == 2:
                print('Out of tries!')
            continue
        else:
            correct_answers += 1
            print('Correct!')
            break

time.sleep(1) # Brief pause to let user see the result
print('Score: %s / %s' % (correct_answers, number_of_questions))
            
