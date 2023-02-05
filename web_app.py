from random import randint
from flask import Flask
from db_connector import getusernamebyid

app = Flask(__name__)


@app.route('/get_user_name/<user_id>', methods={'GET'})

def get_user_name(user_id):

    user_name = getusernamebyid(user_id)
    if not user_name:
        return "<H1 id='Error'>""No such user "+user_id +"</H1>"
    else:
        return "<H1 id='user'>" + user_name[1] + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)
