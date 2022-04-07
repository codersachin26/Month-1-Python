"""
generate_xml.py, It's generate xml file from met museum api data.
        There is one function:
            1. generate_xml:
                    get the list of met museum data from get_object_list function
                    and generate xml file from that data via dicttoxml lib.

    @author: sachin@codeops.tech
"""

from Week_1.generate_csv_from_api.generate_csv import get_object_list
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# xml file name
XML_FILE_NAME = "generated_metmuseum_objects.xml"


def generate_xml():
    """
     get the met museum data from get_object_list function
     and convert it to xml string using dicttoxml lib.
     open new xml file, store xml string data to the file.

     """
    object_data = get_object_list(is_flatten=False)
    xml_data = dicttoxml(object_data, attr_type=False)
    formatted_xml_data = parseString(xml_data).toprettyxml()
    xml_file = open(XML_FILE_NAME, 'w')
    xml_file.write(formatted_xml_data)


if __name__ == "__main__":
    generate_xml()
