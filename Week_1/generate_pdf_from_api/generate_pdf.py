"""
generate_pdf.py, It's generate Pdf file from met museum api data.
        There is one function:
            1. generate_pdf:
                    get the list of met museum data from the get_object_list function
                    and generate pdf file from that data using pdfKit lib.

    @author: sachin@codeops.tech
"""
import logging
import os

import pandas as pd
import pdfkit

from Week_1.generate_csv_from_api.generate_csv import get_object_list


# logger configuration
LOG_FILE_NAME = "generate_pdf.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'

logging.basicConfig(filename=LOG_FILE_NAME,
                    level=LEVEL,
                    format=FORMAT,
                    filemode='w'
                    )

# pdf file name
PDF_FILE_NAME = "generated_metmuseum_objects_table.pdf"

# pdf page size configuration for pdfKit lib.
options = {
    'page-height': '300',
    'page-width': '900',
}


def generate_pdf():
    """
     get the met museum data from get_object_list function
     and create a DataFrame using Pandas,
     convert DataFrame data to html string via using to_html method and
     then generate pdf from that html string by using pdfKit lib.

     """

    logging.info('start generate_pdf() func')
    object_list = get_object_list()
    logging.info('get called get_object_list() func ')
    logging.info(f'get_object_list() func return : {object_list}')
    df = pd.DataFrame(object_list)
    df_html = df.to_html()
    pdfkit.from_string(df_html, PDF_FILE_NAME, options=options)
    logging.info(f'generated pdf file to {os.path.join(os.getcwd(), PDF_FILE_NAME)}')
    logging.info('end generate_pdf() func')


if __name__ == "__main__":
    generate_pdf()
