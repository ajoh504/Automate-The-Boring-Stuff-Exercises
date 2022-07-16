#!python3
# converter.py - upload a file to Google Sheets, then download the file in the
#                specified format. The first command line argument must be
#                the filename, the second command line argument must be one
#                of the following:
#                EXCEL, PDF, ODS, HTML, CSV, TSV


import sys
import ezsheets
from pathlib import Path


class GoogleSheetConverter:
    def __init__(self):
        self.file_name = sys.argv[1]
        self.file_type = sys.argv[2]
        self.ss = lambda: ezsheets.upload(self.file_name)
        self.csv_method_call = lambda ss, i: ss.downloadAsCSV(
            str(Path(self.file_name).stem) + str(i) + ".csv"
        )
        self.tsv_method_call = lambda ss, i: ss.downloadAsTSV(
            str(Path(self.file_name).stem) + str(i) + ".tsv"
        )

    def multi_sheet_converter(self, conversion_method_call):
        """
        :param conversion_method_call: If downloading as CSV or TSV file types,
        only one sheet can be downloaded at a time. Input a lambda function call for
        CSV or TSV file extensions. Download the first sheet, delete it, then
        loop back over to download each subsequent sheet.
        """
        ss = self.ss()
        sheet_count = len(ss.sheetTitles)
        for i in range(sheet_count):
            if i != (sheet_count - 1):
                conversion_method_call(ss, i)
                # remove sheet at 0 index on each iteration
                ss[0].delete()
            else:
                # download final sheet
                conversion_method_call(ss, i)

    def main(self):
        if self.file_type.upper() == "EXCEL":
            self.ss().downloadAsExcel(str(Path(self.file_name).stem) + ".xlsx")
        elif self.file_type.upper() == "PDF":
            self.ss().downloadAsPDF(str(Path(self.file_name).stem) + ".pdf")
        elif self.file_type.upper() == "ODS":
            self.ss().downloadAsODS(str(Path(self.file_name).stem) + ".ods")
        elif self.file_type.upper() == "HTML":
            self.ss().downloadAsHTML(str(Path(self.file_name).stem) + ".html")
        elif self.file_type.upper() == "CSV":
            self.multi_sheet_converter(self.csv_method_call)
        elif self.file_type.upper() == "TSV":
            self.multi_sheet_converter(self.tsv_method_call)
        else:
            print(
                "File type must be one of the following:\nEXCEL, PDF, ODS, HTML, CSV, TSV"
            )


if __name__ == "__main__":
    google_sheet_converter = GoogleSheetConverter()
    google_sheet_converter.main()
