from pprint import pprint


class Config:
    pass


class DevConfig(Config):
    host = 'localhost'
    beyound_host = '192.168.1.187'
    salt = b'i\xca\xe9\x92\x83\xd4n\x04\xe1\x82}\xf5\x8bn\xd7\xc1\xe9\x0f\x07*\xc9mV`H;\r\xd1u\xd6\xe9;'
    PG = {
        'database': 'rusm',
        'db_user': 'postgres',
        'password': 'kat04102004',
        'host': host,
        'port': 5432
    }
