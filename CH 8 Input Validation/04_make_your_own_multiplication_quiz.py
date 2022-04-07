#! python3
# Make your own multiplication quiz

import time, random, re, threading

NUMBER_OF_QUESTIONS = 10
correct_answers = 0

for question_number in range(NUMBER_OF_QUESTIONS):# The first for loop determines the number of questions to ask
    if question_number != 0: # Don't show score on first question
        time.sleep(1) # Brief pause to let user see the result
        print('Score: %s / %s' % (correct_answers, NUMBER_OF_QUESTIONS))
    num1 = random.randint(0, 9) # random number 1
    num2 = random.randint(0, 9) # random number 2
    regex = re.compile(r'^\d+$') #  regex that requires a digit
    prompt = 'Question #%s: %s x %s = ' % (question_number, num1, num2) # prompt is the question to ask the user
    
    for attempt in range(0, 3): # The second for loop allows only 3 attempts per question
        # create a switch and a timeout function that flips the switch
        timeout_switch = False
        def timeout():
            global timeout_switch
            timeout_switch = True
        eight_seconds = threading.Timer(8, timeout) # timeout switch is flipped if timer reaches 0
        eight_seconds.start()  # start timer
        answer = str(input(prompt)) # convert user's answer to string in order to pass it into regex
        mo = regex.search(answer)
        
        if timeout_switch == True:
            print('Out of time!')
            break
        # mo == None helps avoid an AttributeError because mo.group() will throw an error if a non-digit is entered by the user
        elif (mo == None) and (timeout_switch == False):
            eight_seconds.cancel()
            print('Incorrect')
            if attempt == 2:
                print('Out of tries!')
            continue
        elif (int(mo.group()) != (num1 * num2)) and (timeout_switch == False):
            eight_seconds.cancel()
            print('Incorrect!')
            if attempt == 2:
                print('Out of tries!')
            continue
        else:
            eight_seconds.cancel()
            correct_answers += 1
            print('Correct!')          
            break

time.sleep(1) # Brief pause to let user see the result
print('Score: %s / %s' % (correct_answers, number_of_questions))


            
