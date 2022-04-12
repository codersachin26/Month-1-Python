from Week_2.XConvertor.xconvertor import XConvertor
from Week_1.generate_csv_from_api.generate_csv import get_object_list

xObj = XConvertor(get_object_list())
xObj.to_pdf()
xObj.to_csv()
xObj.to_excel()
xObj.to_html()
xObj.to_xml()
