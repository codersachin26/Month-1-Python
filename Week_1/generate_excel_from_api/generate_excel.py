"""
generate_excel.py, It's generate Excel file from api data.
        There is one function:
            1. generate_excel:
                    get the list of met museum data from get_object_list function
                    and call the pandas DataFrame method to_excel to create Excel file.

    @author: sachin@codeops.tech
"""

from Week_1.generate_csv_from_api.generate_csv import get_object_list
import pandas as pd

# Excel file name
EXCEL_FILE_NAME = "generated_metmuseum_objects.xlsx"


def generate_excel():
    """
    create Excel file from met museum data using Pandas DataFrame method,
    get_object_list function return list of met museum objects.

    """
    object_list = get_object_list()
    df = pd.DataFrame(object_list)
    df.to_excel(EXCEL_FILE_NAME, index=False)


if __name__ == "__main__":
    generate_excel()
