import pandas as pd
from Week_1.generate_csv_from_api.generate_csv import get_flatten_object_list

HTML_FILE_NAME = "generated_metmuseum_objects_table.html"

def generate_html():
    object_list = get_flatten_object_list()
    df = pd.DataFrame(object_list)
    df.to_html(HTML_FILE_NAME)


if __name__ == "__main__":
    generate_html()
