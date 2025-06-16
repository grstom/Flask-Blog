import mysql.connector
import uuid


'''
-----------------------------------------------------------------------------------+
| user_cookies | CREATE TABLE `user_cookies` (
  `userid` varchar(40) NOT NULL,
  `session` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE KEY `session` (`session`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci |
'''

class Cookies():
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.userdb = 'mysql'
        self.cookiedb = 'cookies'
    
        self.user_connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            db = self.userdb
        )

        self.cookie_db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            db = self.cookiedb
        )

    def createCookie(self, userid, password):
        try:
            #Check if the account exists in the database first
            user_cursor = self.user_connection.cursor()
            cookie_cursor = self.cookie_db.cursor()


            #check the user database to see if the account is real
            user_cursor.execute('''SELECT 1 from users where id = %s and password = %s LIMIT 1;''', (userid, password))
            result = user_cursor.fetchone()

            # Check to see if that user already 
            # has a cookie in the database.
            # 
            #  
            # If they do -> delete it and make a new one
            # If not -> make a new one

            if result:
                #check with the database if their account is or isnt in there
                cookie_cursor.execute('''SELECT 1 from user_cookies where userid = %s LIMIT 1;''', (userid,))
                checkCookie = cookie_cursor.fetchone()


                # if it dosen't exist, create it
                if not checkCookie:
                    print('Begin creation of trying to create a new cookie')
                    session_id = str(uuid.uuid4())
                    cookie_cursor.execute('''INSERT INTO user_cookies (userid, session) VALUES (%s, %s);''', (userid, session_id))
                    self.cookie_db.commit()
                    print('Created a new cookie')
                    return [True, session_id]
                else:
                    # if there's already one
                    # delete old session entry and replace it with a new one
                    print('Begin updating a cookie')
                    session_id = str(uuid.uuid4())
                    cookie_cursor.execute('''UPDATE user_cookies SET session = %s WHERE userid = %s;''', (session_id, userid))
                    print("Updated a cookie")
                    self.cookie_db.commit()
                    return [True, session_id]

        except Exception as e:
            print(f'Cookie creation error: {e}')

    def getIdByCookie(self, cookie):
        cursor = self.cookie_db.cursor()

        getCookie = cursor.execute('''select userid from user_cookies where session = %s;''', (cookie,))
        getCookie = cursor.fetchone()

        return getCookie[0]