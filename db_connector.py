import pymysql
import datetime

import pymysql.err

schema_name = "freedb_hellosql"
table_name = "users2"
current_date = datetime.datetime.now()


def db_coon():
    try:
        conn = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_ben123',
            passwd='eEvaBGM4zX7J$8*',
            db=schema_name,
        )

    except pymysql.err.OperationalError as e:
        print(e)
    finally:
        cursor = conn.cursor()
        return cursor, conn

def check_if_user_exist(exist_user_id):
    cursor, conn = db_coon()

    cursor.execute(f"Select * From {schema_name}.{table_name} where user_id = '{exist_user_id}'")
    conn.commit()

    row_c = cursor.rowcount
    if row_c == 0:
        return False
    else:
        return True


def getusernamebyid(user_id):
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_ben123', passwd='eEvaBGM4zX7J$8*',
                           db=schema_name)
    cursor = conn.cursor()

    my_sql: str = f"Select user_id,user_name,creation_date from {schema_name}.{table_name} where user_id = '{user_id}'"

    try:
        cursor.execute(my_sql)
        conn.commit()
        record = cursor.fetchone()

        if not record:
            return False
        else:
            return record

    except pymysql.err.IntegrityError as sqlError:
        print("DB Error", sqlError)
        return False

    finally:
        cursor.close()
        conn.close()


def createuserbyid(user_id, user_name):
    cursor, conn = db_coon()
    current_date = datetime.datetime.now()

    try:
        # Execute the SQL command
        my_sql: str = f"INSERT into {schema_name}.{table_name}(user_id, user_name, creation_date) " \
                      f"VALUES('{user_id}','{user_name}','{current_date}')"
        cursor.execute(my_sql)
        conn.autocommit(True)

    except pymysql.err.OperationalError as opeErr:
        return opeErr
    except pymysql.err.DataError as datErr:
        return datErr
    except pymysql.err.IntegrityError as iErr:
        return iErr
    finally:
        cursor.close()
        conn.close()
    return True


def put_user_by_id(user_id, new_user_name):
    cursor, conn = db_coon()

    def check_if_user_exist(exist_user_id):
        cursor.execute(f"Select * From {schema_name}.{table_name} where user_id = '{exist_user_id}'")
        conn.commit()

        row_c = cursor.rowcount
        if row_c == 0:
            return False
        else:
            return True

    if check_if_user_exist(user_id) is True:
        try:
            update_user = f"UPDATE {schema_name}.{table_name} Set user_name = '{new_user_name}' WHERE user_id = '{user_id}'"
            cursor.execute(update_user)
            conn.commit()

            if cursor.rowcount == 0:
                print('nothing to update - same name.')
                return False
            elif cursor.rowcount == 1:
                print('user updated, username:', new_user_name)
                return True

        except pymysql.err.OperationalError as e:
            print(e)
        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            conn.close()

    else:
        print("user not exist, cannot update")
        return

def removeuserbyid(user_id):
    cursor, conn = db_coon()

    if check_if_user_exist(user_id) is True:
        try:
            cursor.execute(f"DELETE FROM {schema_name}.{table_name} WHERE user_id = {user_id}")
            conn.commit()
            return True
        except pymysql.err.OperationalError as e:
                print(e)
        except Exception as ex:
            print(ex)

        finally:
            cursor.close()
            conn.close()

    else:
        return False