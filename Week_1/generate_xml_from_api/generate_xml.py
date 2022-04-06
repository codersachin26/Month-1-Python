
from Week_1.generate_csv_from_api.generate_csv import get_object_list
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


XML_FILE_NAME = "generated_metmuseum_objects.xml"


def generate_xml():
    object_data = get_object_list(is_flatten=False)
    xml_data = dicttoxml(object_data, attr_type=False)
    formatted_xml_data = parseString(xml_data).toprettyxml()
    xml_file = open(XML_FILE_NAME, 'w')
    xml_file.write(formatted_xml_data)



if __name__ == "__main__":
    generate_xml()
