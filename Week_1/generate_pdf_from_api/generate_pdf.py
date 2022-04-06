import pandas as pd
import pdfkit

from Week_1.generate_csv_from_api.generate_csv import get_object_list


PDF_FILE_NAME = "generated_metmuseum_objects_table.pdf"

options = {
    'page-height': '300',
    'page-width': '900',
}

def generate_pdf():
    object_list = get_object_list()
    df = pd.DataFrame(object_list)
    df_html = df.to_html()
    pdfkit.from_string(df_html, PDF_FILE_NAME,options=options)





if __name__ == "__main__":
    generate_pdf()
