import pymysql
import datetime
import pymysql.err as db_exception
from pypika import Query, Table

global conn


# general function to connect to db
def connect():
    global conn
    try:
        conn
    except NameError:
        conn = pymysql.connect(
            host='remotemysql.com', port=3306, user='y4NyM3cDcO', passwd='wh1C20sdyy', db='y4NyM3cDcO'
        )
        conn.autocommit(True)


# get configuration from db by config_name
def get_configurations(config_name):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        config = Table('config')
        q = Query.from_(config).select('*').where(config.config_name == str(config_name))
        query = q.get_sql().replace('"', '')
        cursor.execute(query)
        res = cursor.fetchone()
        cursor.close()
        return res
    except Exception as e:
        print(e)


# insert new user to db by user_id and user_name, add creation date
# insert new user to users_extra table with creation date as datetime type
# throw error if the user already exist
def create_user(user_id, user_name):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        creation_date = datetime.datetime.now()
        users = Table('users')
        q = Query.into(users) \
            .columns('user_id', 'user_name', 'creation_date') \
            .insert(int(user_id), user_name, str(creation_date))
        query = q.get_sql().replace('"', '')
        cursor.execute(query)
        users_extra = Table('users_extra')
        q = Query.into(users_extra) \
            .columns('user_id', 'user_name', 'creation_date') \
            .insert(int(user_id), user_name, creation_date)
        query = q.get_sql().replace('"', '')
        cursor.execute(query)
        cursor.close()
    except db_exception.IntegrityError as e:
        cursor.close()
        print(e)
        raise Exception('id already exists')


# get user from db by user_id
def get_user(user_id):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    users = Table('users')
    q = Query.from_(users).select('*').where(users.user_id == str(user_id))
    query = q.get_sql().replace('"', '')
    cursor.execute(query)
    res = cursor.fetchone()
    cursor.close()
    return res


# update user_name by user_id
def update_user_name(user_id, user_name):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    users = Table('users')
    q = users.update().set(users.user_name, user_name).where(users.user_id == int(user_id))
    query = q.get_sql().replace('"', '')
    cursor.execute(query)
    cursor.close()


# delete user from db by user_id
def delete_user(user_id):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    users = Table('users')
    q = Query.from_(users).delete().where(users.user_id == int(user_id))
    query = q.get_sql().replace('"', '')
    cursor.execute(query)
    res = True if cursor.rowcount == 1 else False
    cursor.close()
    return res


def close_connection():
    global conn
    conn.close()
