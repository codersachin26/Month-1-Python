"""
generate_html.py, It's generate Html file from api data.
        There is one function:
            1. generate_html:
                    get the list of met museum data from get_object_list function
                    and generate html file from that data.

    @author: sachin@codeops.tech
"""
import logging
import os

import pandas as pd
from Week_1.generate_csv_from_api.generate_csv import get_object_list

# logger configuration
LOG_FILE_NAME = "generate_html.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'

logging.basicConfig(filename=LOG_FILE_NAME,
                    level=LEVEL,
                    format=FORMAT,
                    filemode='w'
                    )
# html file name
HTML_FILE_NAME = "generated_metmuseum_objects_table.html"


def generate_html():
    """
    get the met museum data from get_object_list function
    and create a DataFrame using Pandas,
    add <img> tag to the primaryImage & primaryImageSmall column
    and call the pandas DataFrame method to_html to create Html file.
    """

    logging.info('start generate_html() func')
    object_list = get_object_list()

    if object_list == -1:
        logging.debug('get_object_list() func call failed, return -1')
        return

    logging.debug(f'get_object_list() func return : {object_list}')
    df = pd.DataFrame(object_list)
    logging.debug('object_list converted to DataFrame df object')

    df['primaryImage'] = df['primaryImage'].apply(
        lambda url: f'<img src="{url}" height="100" width="100">' if url != '' else '')
    logging.debug('converted df primaryImage column values to <img> tag')

    df['primaryImageSmall'] = df['primaryImageSmall'].apply(
        lambda url: f'<img src="{url}" height="100" width="100">' if url != '' else '')
    logging.debug('converted df primaryImageSmall column values to <img> tag')

    df.to_html(HTML_FILE_NAME, escape=False)
    logging.debug(f'generated Html file to {os.path.join(os.getcwd(), HTML_FILE_NAME)}')
    logging.info('end generate_html() func')


if __name__ == "__main__":
    generate_html()
