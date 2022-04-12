"""
generate_xml.py, It's generate xml file from met museum api data.
        There is one function:
            1. generate_xml:
                    get the list of met museum data from get_object_list function
                    and generate xml file from that data via dicttoxml lib.

    @author: sachin@codeops.tech
"""
import logging
import os

from Week_1.generate_csv_from_api.generate_csv import get_object_list
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# logger configuration
LOG_FILE_NAME = "generate_xml.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'

logging.basicConfig(filename=LOG_FILE_NAME,
                    level=LEVEL,
                    format=FORMAT,
                    filemode='w'
                    )

# xml file name
XML_FILE_NAME = "generated_metmuseum_objects.xml"


def generate_xml():
    """
     get the met museum data from get_object_list function
     and convert it to xml string using dicttoxml lib.
     open new xml file, store xml string data to the file.

     """

    logging.info('start generate_xml() func')
    object_list = get_object_list(is_flatten=False)

    if object_list == -1:
        logging.debug('get_object_list() func call failed, return -1')
        return

    logging.info(f'get_object_list() func call return : {object_list}')
    xml_data = dicttoxml(object_list, attr_type=False)
    logging.debug('dicttoxml() func get called with object_list and generate xml bytes')
    formatted_xml_data = parseString(xml_data).toprettyxml()
    logging.debug(f'generated xml string : {formatted_xml_data}')

    try:
        xml_file = open(XML_FILE_NAME, 'w')
        logging.debug(f'successfully open {XML_FILE_NAME} file')
    except OSError as err:
        logging.debug(f'OS error occurred trying to open {XML_FILE_NAME}, Error: {err}')
        return

    xml_file.write(formatted_xml_data)
    logging.info(f'generated xml file at {os.path.join(os.getcwd(),XML_FILE_NAME)}')


if __name__ == "__main__":
    generate_xml()
