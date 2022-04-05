import json
import requests
from flatten_json import flatten
import pandas as pd

# API endpoints
OBJECT_IDS_ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
OBJECT_ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

# name of the CSV file
CSV_FILE_NAME = "generated_metmuseum_objects_using_pandas.csv"


def generate_csv():
    object_list = get_object_list()
    df = pd.DataFrame(object_list)
    df.to_csv(CSV_FILE_NAME, index=False)


def get_object_list(entry_size=20, is_flatten=True):
    object_ids = get_object_ids(OBJECT_IDS_ENDPOINT)
    object_list = []

    for id in object_ids[:entry_size]:
        object_data = get_object_by_id(OBJECT_ENDPOINT, id)
        if is_flatten:
            flatten_object = flatten(object_data)
            object_list.append(flatten_object)
        else:
            object_list.append(object_data)

    return object_list


# return list of object ids from API
def get_object_ids(api_endpoint):
    res = requests.get(api_endpoint)
    if res.status_code == 200:
        res_body = json.loads(res.text)
        object_ids = res_body['objectIDs']
        return object_ids


# return object by id from API
def get_object_by_id(api_endpoint, id):
    res = requests.get(api_endpoint + str(id))

    if res.status_code == 200:
        res_body = json.loads(res.text)
        return res_body


if __name__ == "__main__":
    generate_csv()
