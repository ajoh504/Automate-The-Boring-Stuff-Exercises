#!python3
# decrypt_pdf_file.py - Walk through a directory and its subdirectories, and prompt
#                       the user to input a password to decrypt the files.
#
#                USAGE: sys.argv[1] = filepath to search for PDFs


import sys
import PyPDF2
from pdfparanoia import EncryptPDFs

dir_to_search = sys.argv[1]


def decrypt_pdf_file(file: str) -> None:
    """
    :param file: input PDF file from calling function. Create a PdfFileReader
    object to determine if the PDF is encrypted. If the PDF is encrypted, prompt
    the user for the encryption password. If the password is correct, decrypt it
    the file and save it. If the password is incorrect, warn the user and continue.
    """
    file_object = open(file, "rb")
    reader = PyPDF2.PdfFileReader(file_object)
    if reader.isEncrypted:
        password = input(f"Please enter the password to decrypt {file}\n")
        if reader.decrypt(password) == 0:
            print(f"Password invalid. {file} was not decrypted\n")
        elif reader.decrypt(password) == 1:
            print(f"Decrypting {file}")
            writer = PyPDF2.PdfFileWriter()
            for page_num in range(reader.numPages):
                writer.addPage(reader.getPage(page_num))
            result_pdf = open(file.split(".")[0] + "_decrypted.pdf", "wb")
            writer.write(result_pdf)
            result_pdf.close()
            print(f"{file} has been decrypted and saved.")
    file_object.close()


DECRYPTION_CALL = decrypt_pdf_file  # store function as Callable

if __name__ == "__main__":
    EncryptPDFs.search_for_pdf(dir_to_search, DECRYPTION_CALL)
