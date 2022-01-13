from abc import ABC


class DatabaseInfo(ABC):
    user = 'root'
    password = '2731'
    host = 'localhost'
    database = 'academy'
    auth_plugin = 'mysql_native_password'
