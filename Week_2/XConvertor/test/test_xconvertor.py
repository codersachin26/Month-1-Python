import os
import unittest
import logging

from Week_2.XConvertor.helpers import get_md5_hash, md5_checksum_for_pdf, zip_files, send_email, sender_email, \
    sender_pass, reciever
from Week_2.XConvertor.xconvertor import XConvertor
from Week_1.generate_csv_from_api.generate_csv import get_object_list

# logger configuration
LOG_FILE_NAME = "test_xconvertor.log"
LEVEL = logging.DEBUG
FORMAT = '[%(asctime)s] : %(levelname)s -> %(message)s'


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
        real_file = os.path.join(os.path.dirname(os.getcwd()), "generated_files_by_xconvertor/x_convertor.csv")

        # get hash values of real & generated file
        real_file_hash = get_md5_hash(real_file)
        test_file_hash = get_md5_hash(test_file)

        self.assertEqual(test_file_hash, real_file_hash)


    def test_html_file_content(self):
        self.convertor.to_html()
        test_file = self.convertor.file_Name + '.html'
        real_file = os.path.join(os.path.dirname(os.getcwd()), "generated_files_by_xconvertor/x_convertor.html")
        real_file_hash = get_md5_hash(real_file)
        test_file_hash = get_md5_hash(test_file)

        self.assertEqual(test_file_hash, real_file_hash)

    def test_xml_file_content(self):
        self.convertor.to_xml()
        test_file = self.convertor.file_Name + '.xml'
        real_file = os.path.join(os.path.dirname(os.getcwd()), "generated_files_by_xconvertor/x_convertor.xml")
        real_file_hash = get_md5_hash(real_file)
        test_file_hash = get_md5_hash(test_file)

        self.assertEqual(test_file_hash, real_file_hash)

    def test_excel_file_content(self):
        import pandas as pd

        self.convertor.to_excel()

        test_file = self.convertor.file_Name + '.xlsx'
        real_file = os.path.join(os.path.dirname(os.getcwd()), "generated_files_by_xconvertor/x_convertor.xlsx")

        real_df = pd.read_excel(real_file, engine='openpyxl')
        test_df = pd.read_excel(test_file, engine='openpyxl')
        match = real_df.equals(test_df)

        self.assertEqual(True, match)

    def test_pdf_file_content(self):
        self.convertor.to_pdf()
        # test & real file path
        test_file = self.convertor.file_Name + '.pdf'
        real_file = os.path.join(os.path.dirname(os.getcwd()), "generated_files_by_xconvertor/x_convertor.pdf")

        test_file_hash = md5_checksum_for_pdf(test_file)
        real_file_hash = md5_checksum_for_pdf(real_file)

        self.assertEqual(test_file_hash, real_file_hash)




class TestResults(unittest.TestResult):


    def addError(self, test, err):
        super(TestResults, self).addError(test, err)
        subject = "Tests Failed - XConvertor"
        body = f"tests:{test} \n Error: {err}"
        zp_file = zip_files("my_zip.zip", ['test_xconvertor.log'])
        send_email(sender_email=sender_email,
                   sender_passwrd=sender_pass,
                   body=body,receiver_email=reciever,
                   zip_file=zp_file,subject=subject)

    def addFailure(self, test, err):
        super(TestResults, self).addFailure(test, err)
        subject = "Tests Failed - XConvertor"
        body = f"tests:{test} \n Error: {err}"
        zp_file = zip_files("my_zip.zip", ['test_xconvertor.log'])
        send_email(sender_email=sender_email,
                   sender_passwrd=sender_pass,
                   body=body, receiver_email=reciever,
                   zip_file=zp_file, subject=subject)

    def addSuccess(self, test):
        super(TestResults, self).addSuccess(test)
        subject = "Tests Pass - XConvertor"
        body = f"tests:{test}"
        zp_file = zip_files("my_zip.zip", ['test_xconvertor.log'])
        send_email(sender_email=sender_email,
                   sender_passwrd=sender_pass,
                   body=body, receiver_email=reciever,
                   zip_file=zp_file, subject=subject)

