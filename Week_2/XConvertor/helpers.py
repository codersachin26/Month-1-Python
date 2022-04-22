import hashlib
import logging

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject


def get_md5_hash(file):
    md5_obj = hashlib.md5()
    try:
        file = open(file)
        file_content = file.read()
        md5_obj.update(file_content.encode('utf-8'))
        file.close()
        return md5_obj.hexdigest()
    except OSError as err:
        logging.error(f'can not open {file} file, Error: {err}')
        return -1


def md5_checksum(data):
    md5_obj = hashlib.md5()
    md5_obj.update(data.encode('utf-8'))
    return md5_obj.hexdigest()


def md5_checksum_for_pdf(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def embedd_metadata_file(file_in, file_out, timeDate,pdfObj):
    with open(file_in, 'rb') as fin:
        pdf = PdfFileReader(fin)
        writer = PdfFileWriter()
        metadata = writer._info.getObject()
        info = pdf.documentInfo
        print(timeDate)
        for page in range(pdf.getNumPages()):
            writer.addPage(pdf.getPage(page))

        for key in info:
            print(info[key])
            metadata.update({NameObject(key): info[key]})

        metadata.update({
            NameObject('/CreationDate'): createStringObject(str(timeDate)),
            NameObject('/NeedAppearances'): pdfObj
        })

        with open(file_out, 'wb') as fout:
            writer.write(fout)

        fin.close()
        fout.close()
