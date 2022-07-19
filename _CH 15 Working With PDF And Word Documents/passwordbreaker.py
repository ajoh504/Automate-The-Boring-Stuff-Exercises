#!python3
# passwordbreaker.py - Take an encrypted PDF file that has a simple English
#                      word as its password, and write a brute force password
#                      breaker that loops through plain English words from a
#                      dictionary.txt file.
#
#               USAGE: sys.argv[1] = encrypted PDF
#                      sys.argv[2] = dictionary.txt

import sys
import PyPDF2


def password_breaker():
    """
    Use list comprehension to create word_list and remove any "\n" characters. Loop
    through word_list. Pass word.upper() and word.lower() into reader.decrypt(). If
    either returns 1, then the password has been cracked.
    """
    word_list = [
        word.split("\n")[0]
        for word in open(sys.argv[2], "r").readlines()
        if "\n" in word
    ]
    file_object = open(sys.argv[1], "rb")
    reader = PyPDF2.PdfFileReader(file_object)
    print('Attempting brute force password break. Please wait...')
    for i, word in enumerate(word_list):
        if reader.decrypt(word.upper()) == 1:
            print(f"Password is {word.upper()}")
            break
        elif reader.decrypt(word.lower()) == 1:
            print(f"Password is {word.lower()}")
            break
        elif i == len(word_list) - 1:
            print(f'Password not found in {sys.argv[2]}')
    file_object.close()


if __name__ == "__main__":
    password_breaker()
