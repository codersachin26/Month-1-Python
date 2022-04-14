import logging

import mysql.connector as mySql_connector
from mysql.connector import errorcode


class SqlDB:
    def __init__(self,username,password,host,database):
        self.conn = None
        """
        connect to mysql server and save the connection object.
        """
        try:
            self.conn = mySql_connector.connect(user=username, password=password, host=host, database=database)
            logging.info('connected to mysql server')
        except mySql_connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error(f"wrong username or password, Error: {repr(err)}")
            else:
                logging.error(f"Something is wrong, Error: {repr(err)}")

    def insert_rows(self,rows):
        """
        insert list of rows into crypto_data table.
        """
        cur = self.conn.cursor()
        sql = "INSERT INTO crypto_data (id,symbol,name,image,current_price,market_cap,market_cap_rank,fully_diluted_valuation,total_volume,high_24h,low_24h,price_change_24h,price_change_percentage_24h,market_cap_change_24h,market_cap_change_percentage_24h,circulating_supply,total_supply,max_supply,ath,ath_change_percentage,ath_date,atl,atl_change_percentage,atl_date,roi,last_updated) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        for row in rows:
            try:
                cur.execute(sql, row)
            except mySql_connector.Error as err:
                logging.error(f'sql query not executed, Error: {repr(err)}')
                return "csv file can't upload."

        self.conn.commit()
        self.conn.close()

        logging.debug('inserted all rows to crypto_data table')

        return "csv file uploaded"




