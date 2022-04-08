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
    logging.info('get called get_object_list() func ')
    logging.info(f'get_object_list() func return : {object_list}')
    xml_data = dicttoxml(object_list, attr_type=False)
    formatted_xml_data = parseString(xml_data).toprettyxml()
    logging.info(f'generated xml string : {formatted_xml_data}')
    xml_file = open(XML_FILE_NAME, 'w')
    xml_file.write(formatted_xml_data)
    logging.info(f'generated xml file at {os.path.join(os.getcwd(),XML_FILE_NAME)}')


if __name__ == "__main__":
    generate_xml()
