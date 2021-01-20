import pymysql

global cursor


def connect():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='y4NyM3cDcO', passwd='wh1C20sdyy', db='y4NyM3cDcO')
    conn.autocommit(True)
    global cursor
    cursor = conn.cursor()


def insertData(table, keys, values):
    cursor.execute('INSERT into y4NyM3cDcO.{} {} VALUES {}'.format(table, keys, values))


