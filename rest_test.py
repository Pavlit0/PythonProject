from flask import Flask, request
from db_connector import getusernamebyid, put_user_by_id
from db_connector import createuserbyid
from db_connector import removeuserbyid

app = Flask(__name__)

# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':

        username = getusernamebyid(user_id)
        if username is False:
            return {"status": "Error", "reason": "ID Not Found", "Code": "500"}, 500  # status code
        else:
            return {"creation_date": username[2], "user name": username[1], "status": "OK", "Code": "200"}, 200  # status code

    elif request.method == 'POST':
        # creating the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # user_id = request_data.get('user_id')

        if createuserbyid(user_id, user_name) is True:
            return {"user id": user_id, "user name": user_name, "status": "OK", "Code": "200"}, 200  # status code
        else:
            return {"status": "Error", "reason": "ID already exist", "Code": "500"}, 500

    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        new_user_name = request_data.get('user_name')

        if put_user_by_id(user_id, new_user_name) is True:
            return {"Status": "OK", "User_Updated": new_user_name, "Code": "200"}, 200
        else:
            return {"status": "error", "reason": "no such id", "Code": "500"}, 500

    elif request.method == 'DELETE':

        isdeleted= removeuserbyid(user_id)

        if isdeleted is True:
            return {"Status": "OK", "user_deleted": user_id, "Code": "200"}, 200
        else:
            return {"status": "error", "reason": "no such id", "Code": "500"}, 500

app.run(host='127.0.0.1', debug=True, port=5000)


