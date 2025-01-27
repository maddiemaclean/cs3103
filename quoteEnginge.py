#!/bin/env python3

import pymysql.cursors
import settings
import cgitb
import cgi
import sys
cgitb.enable()

# Make the connection
dbConnection = pymysql.connect(host=settings.DB_HOST,
				user=settings.DB_USER,
				password=settings.DB_PASSWD,
				database=settings.DB_DATABASE,
				charset='utf8mb4',
				cursorclass= pymysql.cursors.DictCursor)

sql = "getQuote"

def getQuote():
    try:
            cursor = dbConnection.cursor()
            cursor.callproc(sql)
            result = cursor.fetch()
            if result:
                print("""<body>
                             <h1>Random Quote</h1>
                             <p>"{result}" </p>
                          </body>""")

    except pymysql.MySQLError as e:
            print('<p>Ooops - Things messed up: </p>')
    except Exception as e:
            print('<p>Something big went wrong.</p>')
            print(e)

    finally:
        cursor.close()
        dbConnection.close()