import pymysql
import datetime
import pymysql.err as db_exception

global cursor


def connect():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='y4NyM3cDcO', passwd='wh1C20sdyy', db='y4NyM3cDcO')
    conn.autocommit(True)
    global cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)


def create_user(user_id, user_name):
    try:
        creation_date = str(datetime.datetime.now())
        values = (int(user_id), user_name, creation_date)
        cursor.execute('INSERT into y4NyM3cDcO.users (user_id, user_name, creation_date) VALUES {}'.format(values))
    except db_exception.IntegrityError as e:
        print(e)
        raise Exception('id already exists')


def get_user(user_id):
    cursor.execute("SELECT * FROM y4NyM3cDcO.users WHERE user_id = " + user_id)
    return cursor.fetchone()


def update_user_name(user_id, user_name):
    update_data = "user_name = '" + user_name + "'"
    condition = 'user_id = ' + user_id
    cursor.execute("UPDATE y4NyM3cDcO.users SET {} WHERE {}".format(update_data, condition))


def delete_user(user_id):
    condition = 'user_id = ' + user_id
    cursor.execute("DELETE FROM y4NyM3cDcO.users WHERE {}".format(condition))
    return True if cursor.rowcount == 1 else False
