from flask import Flask, render_template, request, jsonify
import sql.user
import sql.cookies
import uuid

db_user = sql.user.Users()
db_cookies = sql.cookies.Cookies()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/logon', methods=['GET', 'POST'])
def logon():
    credential = request.get_json()
    username = credential.get('username')
    password = credential.get('password')

    getId = db_user.getUserId(username, password)
    newCookie = db_cookies.createCookie(getId, password)
    
    return jsonify({'message': 'OK', 'userid': getId, 'sessionid': newCookie[1], 'code': '200'})


@app.route('/register', methods=['GET', 'POST'])
def register():
    #the register logic must check if the account already exists before creating
    #anything
    credential = request.get_json()

    username = credential.get('username')
    password = credential.get('password')
    email = credential.get('email')
    new_id = str(uuid.uuid4())

    subjects = [username, password]
    for everything in subjects:
        if len(everything) >= 25:
            return jsonify({'message': 'Username or password is too long.', 'code': '500'})

    create_user = db_user.createUser(new_id, username, password, email, register=True)

    if not create_user:
        return jsonify({'message': 'The account is already taken.', 'code': '500'})
    else:
        information = db_cookies.createCookie(new_id, password)

        #Return a useable login cookie for the browser
        if information:
            return jsonify({'message': 'Success', 'sessionid': str(information[1]), 'userid': new_id, 'code': '200'})
        else:
            return jsonify({'message': 'Error'})

@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    users = request.get_json()

    username = users.get('userId')
    lookup = db_user.getInformationAboutUser(username)

    if lookup:
        return jsonify({'code': '200', 'userId': str(lookup[0])})
    else:
        return jsonify({'code': '500', 'userId': 'User not found'})

    

    #when this is finished, need to return the new id to
    #the browser. 'db_cookies' should return this.




if __name__ == "__main__":
    app.run(debug=True)