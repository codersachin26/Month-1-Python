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
LEVEL = logging.DEBUG
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

    if object_list == -1:
        logging.error(f'get_object_list() func call failed')
        return

    logging.debug(f'get_object_list() func return : {object_list}')
    df = pd.DataFrame(object_list)
    df.to_csv(CSV_FILE_NAME, index=False)
    logging.debug(f'generated CSV file to {os.path.join(os.getcwd(), CSV_FILE_NAME)}')
    logging.info('generate_csv() func successfully executed')


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

    if not isinstance(entry_size, int) or not isinstance(is_flatten, bool):
        logging.error(
            f'get_object_list() func get called with wrong args, expected entry_size:int & is_flatten:bool but got entry_size:{type(entry_size)} & is_flatten:{type(is_flatten)}')
        return -1

    logging.debug(f'get_object_list() func get called with entry_size={entry_size} & is_flatten={is_flatten}')

    object_ids = get_object_ids(OBJECT_IDS_ENDPOINT)

    if object_ids == -1:
        logging.error(f'get_object_ids() func call failed')
        return -1

    logging.debug(f'get_object_ids() func get called with api Endpoint : {OBJECT_IDS_ENDPOINT} ')
    object_list = []

    for object_id in object_ids[:entry_size]:
        object_data = get_object_by_id(OBJECT_ENDPOINT, object_id)

        if object_data == -1:
            logging.error('get_object_by_id() func call failed')
            break

        logging.debug(f'get called get_object_by_id() func with api Endpoint : {OBJECT_ENDPOINT} & Id : {object_id}')
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
    logging.debug(f'get_object_ids() func get called with API endpoint: {api_endpoint}')

    try:
        res = requests.get(api_endpoint)
    except requests.exceptions.RequestException as e:
        logging.error(f'api call failed : {e}')
        return -1

    if res.status_code == 200:
        logging.debug(f'api response status code : {res.status_code}')
        try:
            res_body = json.loads(res.text)
            logging.debug(f'api response converted into python object ResponseObject: {res_body}')
        except json.decoder.JSONDecodeError as err:
            logging.error(f'json.loads() failed to decode response, Error: {repr(err)}')
            return -1

        object_ids = res_body['objectIDs']
        return object_ids
    else:
        logging.error(f'api response status : {res.status_code}')
        return -1


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
    logging.debug(f'get_object_by_id() func get called with api endpoint : {api_endpoint} with Id : {object_id}')

    try:
        res = requests.get(api_endpoint + str(object_id))
    except requests.exceptions.RequestException as e:
        logging.exception(f'api_endpoint api call failed : {e}')
        return -1

    if res.status_code == 200:
        logging.debug(f'api response status code : {res.status_code}')
        res_body = json.loads(res.text)
        return res_body
    else:
        logging.error(f'api response status code : {res.status_code}')
        return -1


if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE_NAME,
                        level=LEVEL,
                        format=FORMAT,
                        filemode='w'
                        )
    generate_csv()
