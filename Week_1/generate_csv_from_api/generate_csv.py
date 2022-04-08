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
import logging
import os

# logger configuration
LOG_FILE_NAME = "generate_csv.log"
LEVEL = logging.INFO
FORMAT = '%(asctime)s : %(levelname)s -> %(message)s'


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
    logging.info('start generate_csv() func')
    object_list = get_object_list()
    logging.info('get called get_object_list() func ')
    logging.info(f'get_object_list() func return : {object_list}')
    df = pd.DataFrame(object_list)
    df.to_csv(CSV_FILE_NAME, index=False)
    logging.info(f'generated CSV file to {os.path.join(os.getcwd(),CSV_FILE_NAME)}')
    logging.info('end generate_csv()')


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
    logging.info('start get_object_list() func')
    object_ids = get_object_ids(OBJECT_IDS_ENDPOINT)
    logging.info(f'get called get_object_ids() func with api Endpoint : {OBJECT_IDS_ENDPOINT} ')
    object_list = []

    for object_id in object_ids[:entry_size]:
        object_data = get_object_by_id(OBJECT_ENDPOINT, object_id)
        logging.info(f'get called get_object_by_id() func with api Endpoint : {OBJECT_ENDPOINT} & Id : {object_id}')
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
    logging.info('start get_object_ids() func')
    logging.info(f'call api endpoint : {api_endpoint}')
    res = requests.get(api_endpoint)
    logging.info(f'api response status : {res.status_code}')
    if res.status_code == 200:
        res_body = json.loads(res.text)
        object_ids = res_body['objectIDs']
        return object_ids
    else:
        logging.error(f'api response status : {res.status_code}')


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
    logging.info('start get_object_by_id() func')
    logging.info(f'call api endpoint : {api_endpoint} with Id : {object_id}')
    res = requests.get(api_endpoint + str(object_id))
    logging.info(f'api response status : {res.status_code}')

    if res.status_code == 200:
        res_body = json.loads(res.text)
        return res_body
    else:
        logging.error(f'api response status : {res.status_code}')


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE_NAME,
                        level=LEVEL,
                        format=FORMAT,
                        filemode='w'
                        )
    generate_csv()
