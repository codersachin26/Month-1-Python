import csv
import io
from flask import Flask, request, make_response, jsonify

from Week_3.sql_db import SqlDB

# mysql connection credentials
USERNAME = 'sachin'
PASSWORD = 'passwrd#321'
DATABASE = 'crypto_db'
HOST = 'localhost'

app = Flask(__name__)


@app.route('/upload_csv', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']

        with io.TextIOWrapper(f, encoding='utf-8') as text_file:
            reader = csv.DictReader(text_file, delimiter=',')
            data = [list(row.values()) for row in reader]

        db_conn = SqlDB(USERNAME, PASSWORD, HOST, DATABASE)

        if db_conn.conn is None:
            db_msg = "mysql connection error"
        else:
            db_msg = db_conn.insert_rows(data)

        res = make_response(
            jsonify(
                {"message": db_msg}
            ),
        )

        return res


if __name__ == '__main__':
    app.run()
