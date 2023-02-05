from random import randint
from flask import Flask

app = Flask(__name__)

# accessed via <HOST>:<PORT>/get_random
@app.route("/get_random")
def random():
    random_number = randint(1, 10)
    return {'random': random_number}, 200 # status code


# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5000)
