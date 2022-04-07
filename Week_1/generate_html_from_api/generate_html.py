"""
generate_html.py, It's generate Html file from api data.
        There is one function:
            1. generate_html:
                    get the list of met museum data from get_object_list function
                    and generate html file from that data.

    @author: sachin@codeops.tech
"""

import pandas as pd
from Week_1.generate_csv_from_api.generate_csv import get_object_list

# html file name
HTML_FILE_NAME = "generated_metmuseum_objects_table.html"


def generate_html():
    """
    get the met museum data from get_object_list function
    and create a DataFrame using Pandas,
    add <img> tag to the primaryImage & primaryImageSmall column
    and call the pandas DataFrame method to_html to create Html file.
    """
    object_list = get_object_list()
    df = pd.DataFrame(object_list)
    df['primaryImage'] = df['primaryImage'].apply(
        lambda url: f'<img src="{url}" height="100" width="100">' if url != '' else '')
    df['primaryImageSmall'] = df['primaryImageSmall'].apply(
        lambda url: f'<img src="{url}" height="100" width="100">' if url != '' else '')
    df.to_html(HTML_FILE_NAME, escape=False)


if __name__ == "__main__":
    generate_html()
