import mysql.connector
import sql.cookies
import datetime
import uuid


cookieDb = sql.cookies.Cookies()


class Posts():
    def __init__(self):

        self.user = 'root'
        self.password = ''
        self.hostname = 'localhost'
        self.dbname = 'posts'

        self.postDb = mysql.connector.connect (
            host = self.hostname,
            user = self.user,
            password = self.password,
            db = self.dbname
        )

    def CreatePost(self, text, cookie):
        newPostId = str(uuid.uuid4())
        userID = cookieDb.getIdByCookie(cookie)
        cursor = self.postDb.cursor()

        date = datetime.datetime.now().strftime("%Y-%m-%d")
        time = datetime.datetime.now().strftime("%H:%M:%S")

        cursor.execute('''insert into posts (post, date, time, owner, postid) values (%s, %s, %s, %s, %s)''', (text, date, time, userID, newPostId))
        self.postDb.commit()
        return True