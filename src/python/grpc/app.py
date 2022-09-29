# this module is the flask app to server the gRCP client
#
# this module has the following classes:
#     app: this class is used to create the flask app
#
# this module has the following functions:
#     main: this function is used to start the flask app

import grpc

from flask import Flask, request, jsonify

from datetime import date

from client import UsersClient

from obj import User

app = Flask(__name__)

# create a new client
client = UsersClient(grpc.insecure_channel('localhost:50051'))

@app.route('/users', methods=['POST'])
def create_user():
    """
    this method is used to create a user
    :return: a json object
    """

    # get the data from the request
    data = request.get_json()

    # create a new user from the data
    user = User(dob=date.fromisoformat(data['dob']) ,name=data['name'], company=data['company'], phone=data['phone'], title=data['title'])

    # create the user
    user = client.create_user(user)

    # return the user
    return jsonify(user)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """
    this method is used to get a user
    :return: a json object
    """

    # get the user
    user = client.get_user(id)

    # return the user
    return jsonify(user)

# start the app if main
if __name__ == '__main__':
    app.run('0.0.0.0', port = "8080")
