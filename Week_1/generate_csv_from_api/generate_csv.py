"""
    generate_csv.py, It's used to create csv file from met museum API objects data.

    There are four functions:
                1. generate_csv:
                        get the met museum data by calling the get_object_list function
                        and generate csv file from that data.

                2. get_object_list:
                        hit the APIs by requests lib and return the response data.

                        there are two different API call:
                                first one for list of ids.
                                second one for met museum object data.

                3. get_object_ids:
                        hit the API and return the list of met museum ids.


                4. get_object_by_id:
                        hit the API and return the met museum object.


  @author: sachin@codeops.tech

"""


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
    """
    generate csv file from met museum api data,
    get_object_list function return the met museum api data.

    """
    object_list = get_object_list()
    df = pd.DataFrame(object_list)
    df.to_csv(CSV_FILE_NAME, index=False)


def get_object_list(entry_size=40, is_flatten=True):
    """
    return a list of met museum objects data via calling get_object_ids
    and get_object_by_id functions.

    Parameters
    ----------
    entry_size : int
        default -> 10
        length of objects.

    is_flatten : bool
        default -> True
        if True -> return objects with flatten operation.
        if False -> return objects without flatten.

    Returns
    -------
    list of met museum objects.

    """
    object_ids = get_object_ids(OBJECT_IDS_ENDPOINT)
    object_list = []

    for object_id in object_ids[:entry_size]:
        object_data = get_object_by_id(OBJECT_ENDPOINT, object_id)
        if is_flatten:
            flatten_object = flatten(object_data)
            object_list.append(flatten_object)
        else:
            object_list.append(object_data)

    return object_list


# return list of object ids from API
def get_object_ids(api_endpoint):
    """
    hit the api and return list of ids from api response.

    Parameters
    ----------
    api_endpoint : str
        api endpoint url.

    Returns
    -------
    list of met museum ids.

    """
    res = requests.get(api_endpoint)
    if res.status_code == 200:
        res_body = json.loads(res.text)
        object_ids = res_body['objectIDs']
        return object_ids


# return object by id from API
def get_object_by_id(api_endpoint, object_id):
    """
    hit the api and return met museum object from api response.

    Parameters
    ----------
    api_endpoint : str
        met museum api endpoint url.

    object_id : int
        met museum id number.

    Returns
    -------
    met museum object.

    """
    res = requests.get(api_endpoint + str(object_id))

    if res.status_code == 200:
        res_body = json.loads(res.text)
        return res_body


if __name__ == "__main__":
    generate_csv()
