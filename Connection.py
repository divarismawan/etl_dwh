import  pymysql

def connect(db_name_args):

    db_par = pymysql.connect(
        user='root',
        password='',
        host='localhost',
        database=db_name_args
    )

    return db_par