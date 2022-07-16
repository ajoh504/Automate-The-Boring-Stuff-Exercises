#!python3
# pdfparanoia.py - Walk through a directory and its subdirectories, and encrypt
#                  every PDF file. Provide the encryption password via command
#                  line and the filepath to search through.
#
#                  USAGE:
#                  sys.argv[1] = password
#                  sys.argv[2] = filepath to search for PDFs

import os
import sys
import PyPDF2


class EncryptPDFs:
    def __init__(self):
        self.password = sys.argv[1]
        self.dir_to_search = sys.argv[2]

    def encrypt_pdf(self, file: str) -> None:
        reader = PyPDF2.PdfFileReader(open(file, 'rb'))
        writer = PyPDF2.PdfFileWriter()
        for page_num in range(reader.numPages):
            writer.addPage(reader.getPage(page_num))
        writer.encrypt(self.password)
        result_pdf = open(file.split()[0] + '_encrypted.pdf', 'wb')
        writer.write(result_pdf)
        result_pdf.close()

    def walk_dir(self) -> None:
        for folder, sub_folders, file_list in os.walk(self.dir_to_search):
            for file in file_list:
                if file.split('.')[-1].lower() == 'pdf':
                    self.encrypt_pdf(file)

    def check_encrypted_file(self):
        pass

    def delete_file(self):
        pass


if __name__ == "__main__":
    encrypt_pdfs = EncryptPDFs()
