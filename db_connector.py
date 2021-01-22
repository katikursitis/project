import pymysql
import datetime
import pymysql.err as db_exception

global conn


def connect():
    global conn
    try:
        conn
    except NameError:
        conn = pymysql.connect(
            host='remotemysql.com', port=3306, user='y4NyM3cDcO', passwd='wh1C20sdyy', db='y4NyM3cDcO'
        )
        conn.autocommit(True)


def create_user(user_id, user_name):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        creation_date = str(datetime.datetime.now())
        values = (int(user_id), user_name, creation_date)
        cursor.execute('INSERT into y4NyM3cDcO.users (user_id, user_name, creation_date) VALUES {}'.format(values))
        cursor.close()
    except db_exception.IntegrityError as e:
        cursor.close()
        print(e)
        raise Exception('id already exists')


def get_user(user_id):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM y4NyM3cDcO.users WHERE user_id = " + user_id)
    res = cursor.fetchone()
    cursor.close()
    return res


def update_user_name(user_id, user_name):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    update_data = "user_name = '" + user_name + "'"
    condition = 'user_id = ' + user_id
    cursor.execute("UPDATE y4NyM3cDcO.users SET {} WHERE {}".format(update_data, condition))
    cursor.close()


def delete_user(user_id):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    condition = 'user_id = ' + user_id
    cursor.execute("DELETE FROM y4NyM3cDcO.users WHERE {}".format(condition))
    res = True if cursor.rowcount == 1 else False
    cursor.close()
    return res
