"""
generate_excel.py, It's generate Excel file from api data.
        There is one function:
            1. generate_excel:
                    get the list of met museum data from get_object_list function
                    and call the pandas DataFrame method to_excel to create Excel file.

    @author: sachin@codeops.tech
"""
import logging
import os

from Week_1.generate_csv_from_api.generate_csv import get_object_list
import pandas as pd


# logger configuration
LOG_FILE_NAME = "generate_excel.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'

logging.basicConfig(filename=LOG_FILE_NAME,
                    level=LEVEL,
                    format=FORMAT,
                    filemode='w'
                    )

# Excel file name
EXCEL_FILE_NAME = "generated_metmuseum_objects.xlsx"


def generate_excel():
    """
    create Excel file from met museum data using Pandas DataFrame method,
    get_object_list function return list of met museum objects.

    """
    logging.info('start generate_excel() func')
    object_list = get_object_list()
    logging.info('get called get_object_list() func ')
    logging.info(f'get_object_list() func return : {object_list}')
    df = pd.DataFrame(object_list)
    df.to_excel(EXCEL_FILE_NAME, index=False)
    logging.info(f'generated Excel file to {os.path.join(os.getcwd(), EXCEL_FILE_NAME)}')
    logging.info('end generate_excel() func')


if __name__ == "__main__":
    generate_excel()
