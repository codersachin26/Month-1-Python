from Week_1.generate_csv_from_api.generate_csv import get_object_list
import pandas as pd

EXCEL_FILE_NAME = "generated_metmuseum_objects.xlsx"


def generate_excel():
    object_list = get_object_list()
    df = pd.DataFrame(object_list)
    df.to_excel(EXCEL_FILE_NAME, index=False)


if __name__ == "__main__":
    generate_excel()
