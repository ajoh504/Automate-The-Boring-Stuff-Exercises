#!python3
# pdfparanoia.py - Walk through a directory and its subdirectories, and encrypt
#                  every PDF file. Provide the encryption password via command
#                  line and the filepath to search through.
#
#                  USAGE:
#                  sys.argv[1] = password
#                  sys.argv[2] = filepath to search for PDFs
# todo: debug check_encrypted_file() function

import os
import sys
from typing import Callable

import PyPDF2


class EncryptPDFs:
    def __init__(self):
        self.password = sys.argv[1]
        self.dir_to_search = sys.argv[2]
        self.encryption_call = self.encrypt_pdf
        self.delete_call = self.delete_file

    def encrypt_pdf(self, file: str) -> None:
        file_object = open(file, "rb")
        reader = PyPDF2.PdfFileReader(file_object)
        if not reader.isEncrypted:
            writer = PyPDF2.PdfFileWriter()
            for page_num in range(reader.numPages):
                writer.addPage(reader.getPage(page_num))
            writer.encrypt(self.password)
            result_pdf = open(file.split(".")[0] + "_encrypted.pdf", "wb")
            writer.write(result_pdf)
            # if self.decryption_check(file, reader) is None:
            #     print('Warning. ' + file + ' was not encrypted.')
            file_object.close()
            result_pdf.close()
        self.encryption_check(file)
        file_object.close()

    def walk_dir(self, function_call: Callable) -> None:
        print("Searching for .pdf files in: " + '"' + self.dir_to_search + '"')
        for folder, sub_folders, file_list in os.walk(self.dir_to_search):
            for file in file_list:
                if file.split(".")[-1].lower() == "pdf":
                    function_call(file)

    def encryption_check(self, file: str) -> int:
        file_object = open(file, "rb")
        reader = PyPDF2.PdfFileReader(file_object)
        if reader.isEncrypted:
            x = reader.decrypt(self.password)
            file_object.close()
            return x
        file_object.close()
        return -1

    def delete_file(self, file: str) -> None:
        file_object = open(file, "rb")
        reader = PyPDF2.PdfFileReader(file_object)
        if not reader.isEncrypted:
            file_object.close()
            os.remove(file)

    def main(self) -> None:
        self.walk_dir(self.encryption_call)
        # self.walk_dir(self.delete_call)


if __name__ == "__main__":
    encrypt_pdfs = EncryptPDFs()
    encrypt_pdfs.main()
