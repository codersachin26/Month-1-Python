import pandas as pd
from Week_1.generate_csv_from_api.generate_csv import get_flatten_object_list
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

PDF_FILE_NAME = "generated_metmuseum_objects_table.pdf"


def generate_pdf():
    object_list = get_flatten_object_list()
    df = pd.DataFrame(object_list)

    fig, ax = plt.subplots(figsize=(16, 5))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    pdf = PdfPages(PDF_FILE_NAME)
    pdf.savefig(fig, bbox_inches='tight')
    pdf.close()


if __name__ == "__main__":
    generate_pdf()
