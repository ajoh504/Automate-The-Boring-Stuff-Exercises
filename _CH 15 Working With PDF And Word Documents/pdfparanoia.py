#!python3
# pdfparanoia.py - Walk through a directory and its subdirectories, and encrypt
#                  every PDF file. Provide the encryption password via command
#                  line and the filepath to search through. Check to see if
#                  encryption succeeded by attempting to read and decrypt the
#                  files. Prompt the user to delete the older unencrypted files.
#
#                  USAGE:
#                  sys.argv[1] = password
#                  sys.argv[2] = filepath to search for PDFs


import os
import sys
import PyPDF2
from typing import Callable


class EncryptPDFs:
    def __init__(self):
        self.password = sys.argv[1]
        self.dir_to_search = sys.argv[2]
        self.encryption_call = self.encrypt_pdf # variable contains callable
        self.delete_call = self.delete_file # variable contains callable
        self.encryption_check_call = self.encryption_checker # variable contains callable

    def encrypt_pdf(self, file: str) -> None:
        """
        :param file: Input PDF file name from the calling function (walk_dir()).
        If the PDF is not encrypted, create a PDFFileWriter object to encrypt
        and save it as a new file. Encrypted files will be skipped.
        """
        file_object = open(file, "rb")
        reader = PyPDF2.PdfFileReader(file_object)
        if not reader.isEncrypted:
            print(f"Encrypting {file}")
            writer = PyPDF2.PdfFileWriter()
            for page_num in range(reader.numPages):
                writer.addPage(reader.getPage(page_num))
            writer.encrypt(self.password)
            result_pdf = open(file.split(".")[0] + "_encrypted.pdf", "wb")
            writer.write(result_pdf)
            result_pdf.close()
        file_object.close()

    def walk_dir(self, function_call: Callable) -> None:
        """
        :param function_call: Input callable as argument and pass it the file variable.
        Callable argument acts on all PDF files in the given directory tree.
        """
        print("Searching for .pdf files in: " + '"' + self.dir_to_search + '"')
        for folder, sub_folders, file_list in os.walk(self.dir_to_search):
            for file in file_list:
                if file.split(".")[-1].lower() == "pdf":
                    function_call(file)

    def encryption_checker(self, file: str) -> None:
        """Check to see if encryption succeeded by reading and decrypting the files."""
        file_object = open(file, "rb")
        reader = PyPDF2.PdfFileReader(file_object)
        try:
            reader.getPage(0)
        except PyPDF2.utils.PdfReadError:
            print(f"Encryption check 1: {file} cannot be read.")
        if reader.isEncrypted:
            print(
                f"Encryption check 2: isEncrypted() method returns True when called on {file}."
            )
            print(f"{file} is encrypted.\n")
            reader.decrypt(self.password)
        file_object.close()

    def delete_file(self, file: str) -> None:
        file_object = open(file, "rb")
        reader = PyPDF2.PdfFileReader(file_object)
        if not reader.isEncrypted:
            file_object.close()
            os.remove(file)

    def main(self) -> None:
        self.walk_dir(self.encryption_call)
        print("\nSearching for encrypted files to check.\n")
        self.walk_dir(self.encryption_check_call)
        while True:
            choice = input("\nDo you wish to delete all unencrypted files? Y/N\n")
            if choice.upper() == "Y":
                self.walk_dir(self.delete_call)
                break
            elif choice.upper() == "N":
                break
            else:
                continue


if __name__ == "__main__":
    encrypt_pdfs = EncryptPDFs()
    encrypt_pdfs.main()
