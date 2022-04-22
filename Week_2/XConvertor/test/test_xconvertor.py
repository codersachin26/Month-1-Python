import os
import unittest

import PyPDF2

from Week_2.XConvertor.helpers import get_md5_hash, md5_checksum, md5_checksum_for_pdf, embedd_metadata_file
from Week_2.XConvertor.xconvertor import XConvertor
from Week_1.generate_csv_from_api.generate_csv import get_object_list


class TestXConvertor(unittest.TestCase):
    # store XConvertor object
    def setUp(self):
        convertor = XConvertor(get_object_list())
        convertor.file_Name = "generated_file_by_testing/x_convertor"
        self.convertor = convertor

    def test_csv_file_content(self):
        # generate csv file
        self.convertor.to_csv()
        test_file = self.convertor.file_Name + '.csv'
        real_file = os.path.join(os.path.dirname(os.getcwd()),"generated_files_by_xconvertor/x_convertor.csv")

        # get hash values of real & generated file
        real_file_hash = get_md5_hash(real_file)
        test_file_hash = get_md5_hash(test_file)

        self.assertEqual(test_file_hash,real_file_hash)

    def test_html_file_content(self):
        self.convertor.to_html()
        test_file = self.convertor.file_Name + '.html'
        real_file = os.path.join(os.path.dirname(os.getcwd()),"generated_files_by_xconvertor/x_convertor.html")
        real_file_hash = get_md5_hash(real_file)
        test_file_hash = get_md5_hash(test_file)

        self.assertEqual(test_file_hash,real_file_hash)

    def test_xml_file_content(self):
        self.convertor.to_xml()
        test_file = self.convertor.file_Name + '.xml'
        real_file = os.path.join(os.path.dirname(os.getcwd()),"generated_files_by_xconvertor/x_convertor.xml")
        real_file_hash = get_md5_hash(real_file)
        test_file_hash = get_md5_hash(test_file)

        self.assertEqual(test_file_hash,real_file_hash)

    def test_excel_file_content(self):
        import pandas as pd

        self.convertor.to_excel()

        test_file = self.convertor.file_Name + '.xlsx'
        real_file = os.path.join(os.path.dirname(os.getcwd()),"generated_files_by_xconvertor/x_convertor.xlsx")

        df = pd.read_excel(real_file, engine='openpyxl')
        real_data = df.to_csv()
        real_file_hash = md5_checksum(real_data)

        df = pd.read_excel(test_file, engine='openpyxl')
        test_data = df.to_csv()
        test_file_hash = md5_checksum(test_data)

        self.assertEqual(test_file_hash,real_file_hash)

    def test_pdf_file_content(self):

        self.convertor.to_pdf()

        test_file = self.convertor.file_Name + '.pdf'
        real_file = os.path.join(os.path.dirname(os.getcwd()),"generated_files_by_xconvertor/x_convertor.pdf")

        real_file_hash = md5_checksum_for_pdf(real_file)


        pdf_file_obj = open(real_file, 'rb')
        pdfreader = PyPDF2.PdfFileReader(pdf_file_obj)
        creation_date = pdfreader.documentInfo["/CreationDate"]
        pdfObj = pdfreader.documentInfo["/CreationDate"]


        embedd_metadata_file(test_file, test_file, creation_date,pdfObj)
        test_file_hash = md5_checksum_for_pdf(test_file)

        self.assertEqual(test_file_hash, real_file_hash)







