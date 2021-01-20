import src.models.dal as db
import pymysql.err as db_exception

table = 'users'


def save(user_id, user_name):
    try:
        db.insertData(table, '(id, name)', (int(user_id), user_name))
    except db_exception.IntegrityError as e:
        print(e)
        raise Exception('id already exists')

