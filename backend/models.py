import utils
from exceptions import Login_Error
from cfg import DevConfig as cfg
from pprint import pprint
con = utils.create_connection(*cfg.PG.values())
#con = utils.create_connection(*cfg.PG.values())
class User:
    pass
class User_Web(User):
       
    def register_user(self, payload):
        try:
            self.login, self.password  = payload['login'], utils.hash_password(payload['password'])
            with con.cursor() as cur:
                cur.execute(
                f"SELECT id FROM users where login = '{self.login}'"
                )
                res = cur.fetchall()
                if res:
                    return '401'
                else:
                    with con.cursor() as cur:
                        cur.execute(
                            f"INSERT INTO users (login, password) VALUES ('{self.login}', '{self.password}')"
                        )
                        con.commit()
                        return '200'
        except Exception as e:
            print(e)
    def register_education(self, payload):
        try:
            self.group = '_'.join(payload.values).lower()
            
            with con.cursor() as cur:
                cur.execute(
                    f"SELECT id WHERE groupe = '{self.group}'"
                )
                res = cur.fetchall()
                if res:
                    return '401'
                else:
                    with con.cursor() as cur:
                        cur.execute(
                            f"INSERT INTO users (groupe) VALUES ('{self.group}')"
                        )
                        con.commit()
                        return '200'
        except Exception as e:
            print(e)
    def login_check(self, payload):
        try:
            self.login, self.password = payload['login'], payload['password']
            with con.cursor() as cur:
                cur.execute(
                    f"SELECT password FROM users WHERE login='{self.login}'"
                )
                res=cur.fetchone()[0]
                if utils.check_password(payload['password'], res): # => b'asdasdas'.encode('utf-8') => 
                    return '200'
                else:
                    raise Login_Error
        except Exception as e:
            print(e)
    def get_group(self):
        try:
            with con.cursor() as cur:
                cur.execute(
                    f"SELECT groupe FROM users WHERE login='{self.login}'"
                )
                res = cur.fetchone()
                return res[0]  
        except Exception as e:
            print(e)
        
class User_Bot(User):
    pass
class Task:
    def add_task(self, payload, user):
        try:
            group = user.get_group()
            with con.cursor() as cur:
                cur.execute(
                    f"INSERT INTO tasks (groupe, task, author, date, subject) VALUES ('{group}', '{payload['task']}', '{user.login}', '{payload['date']}', '{payload['subject']}')"
                )
                con.commit()
                return '200'
        except Exception as e:
            print(e)
    def get_task(self, payload, user):
        try:
            date = payload['date']
            with con.cursor() as cur:
                cur.execute(
                    f"SELECT id, subject, task, author FROM tasks WHERE date = '{date}' AND groupe = '{user.get_group()}'"
                )
                response = cur.fetchall()
                return [{
                    'id': res[0],
                    'subject': res[1],
                    'task': res[2],
                    'author': res[3]
                } for res in response] # => [el**2 for el in list]
        except Exception as e:
            print(e)
            
    def delete_task(self, payload, user):
        try:
            id = payload['id']
            with con.cursor() as cur:
                cur.execute(
                    f"DELETE group, task, author, date, subject FROM tasks WHERE id ={id} AND author = '{user.login}'"
                )
                con.commit()
                return '200'
        except Exception as e:
            print(e)
