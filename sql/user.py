import mysql.connector
import uuid
import emoji


'''| users | CREATE TABLE `users` (
  `id` char(36) NOT NULL,
  `username` varchar(25) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci |'''


class Users():
    def __init__(self):
        self.connection = None
        self.host = 'localhost'
        self.password = ''
        self.user = 'root'
        self.database = 'mysql'



        self.connection = mysql.connector.connect(
            host = self.host,
            password = self.password,
            user = self.user,
            database = self.database
        )
    
    def createUser(self, new_uuid, username, password, email, register):
        check_emoji = any(char in emoji.EMOJI_DATA for char in username)

        # if '' in username or '' in email or check_emoji or '' in password:
        #     return ['1', 'fields cannot be blank']
        # else:

        try:
            if register:
                cursor = self.connection.cursor()
                cursor.execute('''SELECT 1 from users where username=%s and email = %s LIMIT 1;''', (username, email))
                checkAccountAlreadyExist = cursor.fetchone()

                if checkAccountAlreadyExist:
                    return False
                else:
                    cursor = self.connection.cursor()
                    cursor.execute('''INSERT INTO users (id, username, password, email) values (%s, %s, %s, %s) ''', (new_uuid, username, password, email))
                    self.connection.commit()
                    return True
        except Exception as e:
            print('Exception:', e)

    def changePassword(self, uuid, old_password, new_password):
        try:
            cursor = self.connection.cursor()
            
            #Check to see if the old password matches
            old = cursor.execute('''SELECT password from users where password = %s and id = %s;''',(old_password, uuid))
            old = cursor.fetchone()
            print(old[0])

            if old_password == old[0]:
                cursor.execute("""UPDATE users SET password = %s where id = %s""", (new_password, uuid))
                self.connection.commit()
                print('ok')
            else:
                print('Old password does not match')

        except mysql.connector.errors.IntegrityError:
            print('Error: illegal entry')
        except TypeError:
            print('Error: new password cannot be same as old password')
    
    def getUserId(self, username, password):
        cursor = self.connection.cursor()

        getUserId = cursor.execute('''select id from users where username=%s and password=%s;''', (username, password))
        getUserId = cursor.fetchone()

        return getUserId[0]

    def getInformationAboutUser(self, userid):
        cursor = self.connection.cursor()

        getUserInformation = cursor.execute("SELECT username FROM users WHERE id = %s", (userid,))
        result = cursor.fetchone()
        return result
    