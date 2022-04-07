import pandas as pd
from Week_1.generate_csv_from_api.generate_csv import get_object_list

HTML_FILE_NAME = "generated_metmuseum_objects_table.html"


def generate_html():
    object_list = get_object_list()
    df = pd.DataFrame(object_list)
    df['primaryImage'] = df['primaryImage'].apply(
        lambda url: f'<img src="{url}" height="100" width="100">' if url != '' else '')
    df['primaryImageSmall'] = df['primaryImageSmall'].apply(
        lambda url: f'<img src="{url}" height="100" width="100">' if url != '' else '')
    df.to_html(HTML_FILE_NAME, escape=False)


if __name__ == "__main__":
    generate_html()
