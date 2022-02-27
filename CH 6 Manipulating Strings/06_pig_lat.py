# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = [] # A list of the words in Pig Latin.

for word in message.split():
    # Separate the non-letters at the start of this word:
    prefix_nonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_nonletters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_nonletters)
        continue
    # Separate the non-letters at the end of this word:
    suffix_nonletters = ''
    while not word[-1].isalpha():
        suffix_nonletters += word[-1]
        word = word[:-1]
    # Remember if word was in uppercase or title case
    was_upper = word.isupper()
    was_title = word.istitle()
    word = word.lower() # Make the word lowercase for translation
    # Separate the consonants at the start of this word:
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        word = word[1:]
    # Add the pig latin ending to the word:
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    # add the non-letters back to the start or the end of the word
    pig_latin.append(prefix_nonletters + word + suffix_nonletters)
    # Join all the words back together into a single string:
    print(' '.join(pig_latin))
    
