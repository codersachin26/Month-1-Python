import json
import requests
from flatten_json import flatten
import pandas as pd

# API endpoints
OBJECT_IDS_ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
OBJECT_ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

# name of the CSV file
CSV_FILE_NAME = "generated_metmuseum_objects_using_pandas.csv"


def generate_csv(entry_size=20):
    object_ids = get_object_ids(OBJECT_IDS_ENDPOINT)
    object_list = []

    for id in object_ids[:entry_size]:
        object_data = get_object_by_id(OBJECT_ENDPOINT, id)
        flatten_object = flatten(object_data)
        object_list.append(flatten_object)

    df = pd.DataFrame(object_list)
    df.to_csv(CSV_FILE_NAME, index=False)


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


generate_csv()
