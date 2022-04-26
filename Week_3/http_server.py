import logging

from flask import Flask, request, make_response, jsonify, render_template

from Week_3.helpers import csv_to_list
from Week_3.sql_db import SqlDB
import mysql.connector as mySql_connector

# mysql connection credentials
USERNAME = 'sachin'
PASSWORD = 'passwrd#321'
DATABASE = 'crypto_db'
HOST = 'localhost'

app = Flask(__name__)


@app.route('/insert_into_db', methods=['POST', 'GET'])
def insert_to_db():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        csv_file = request.files['file']

        db_conn = SqlDB(USERNAME, PASSWORD, HOST, DATABASE)

        if not db_conn.is_connected():
            msg = "mysql connection error"
        else:
            if db_conn.insert_from_csv(csv_file) == 1:
                msg = f"successfully inserted csv file {csv_file.filename} data into db"
            else:
                msg = "can't insert csv to db"

        db_conn.close_conn()
        res = make_response(
            jsonify(
                {"message": msg}
            ),
        )

        return res


@app.route('/upload_to_table', methods=['POST', 'GET'])
def upload_csv():
    if request.method == 'POST':
        file = request.files['file']

        csv_data = csv_to_list(file)

        if csv_data == -1:
            msg = 'not able to read csv file'
        else:
            db_conn = SqlDB(USERNAME, PASSWORD, HOST, DATABASE)

            if db_conn._conn is None:
                msg = "mysql connection error"
            else:
                msg = db_conn.insert_rows(csv_data)

        res = make_response(
            jsonify(
                {"message": msg}
            ),
        )

        return res

    elif request.method == 'GET':
        return render_template('index.html')


@app.route('/insert/<string:table_name>', methods=['POST'])
def insert_rows(table_name):
    """
    insert_rows(table_name), add rows to existing table.
    """
    json_data = request.get_json()
    rows_data = json_data.get('rows')
    rows = [list(row.values()) for row in rows_data]

    db_conn = SqlDB(USERNAME, PASSWORD, HOST, DATABASE)
    if not db_conn.is_connected():
        msg = 'mysql server not connected'
        logging.error(msg)
        return make_response(msg)

    if db_conn.check_table_exist(table_name):
        try:
            db_conn.insert_into_table(table_name, rows)
            logging.debug(f'rows added to {table_name} table')
            res = f'successfully inserted rows to {table_name} table'
        except mySql_connector.errors.OperationalError as err:
            logging.error(f"can't insert rows to {table_name} table, Error: {repr(err)}")
            res = jsonify({'message': f"can't insert rows to {table_name} table"})
    else:
        res = jsonify({'message': f"{table_name} table not exist"})
        logging.error(f"{table_name} table not exist")

    db_conn.close_conn()
    return make_response(res)


@app.route('/read/<string:table_name>', methods=['GET'])
def read_rows(table_name):
    db_conn = SqlDB(USERNAME, PASSWORD, HOST, DATABASE)
    if not db_conn.is_connected():
        msg = 'mysql server not connected'
        logging.error(msg)
        return make_response(msg)

    rows_data = db_conn.read_rows(table_name)

    if rows_data != -1:
        res = jsonify(rows_data)
    else:
        msg = f'something wrong,can not read from {table_name} table'
        res = {"msg": msg}

    db_conn.close_conn()

    return make_response(res)


@app.route('/delete/<string:table_name>/<string:item_id>', methods=['DELETE'])
def delete_rows(table_name, item_id):
    db_conn = SqlDB(USERNAME, PASSWORD, HOST, DATABASE)
    if not db_conn.is_connected():
        msg = 'mysql server not connected'
        logging.error(msg)
        return make_response(msg)

    if db_conn.delete_row(table_name, item_id) != -1:
        res = f'row deleted from {table_name} table'
    else:
        res = f'row did not deleted from {table_name} table'

    return make_response(jsonify({"msg": res}))


@app.route('/update/<string:table_name>/<string:item_id>', methods=['PUT'])
def update_rows(table_name, item_id):
    """
    update_rows() func, update single record in a table.
    """
    json_data = request.get_json()

    # make connection to database
    db_conn = SqlDB(USERNAME, PASSWORD, HOST, DATABASE)
    if not db_conn.is_connected():
        msg = 'mysql server not connected'
        logging.error(msg)
        return make_response({"msg": msg})

    if db_conn.update_row(table_name, item_id, json_data) == 1:
        res = f'successfully updated record in {table_name} table'
        logging.info(res)
    else:
        res = f'update get failed in {table_name} table'
        logging.error(res)

    return make_response(jsonify({"msg": res}))


if __name__ == '__main__':
    app.run(debug=True)
