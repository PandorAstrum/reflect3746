from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/api/v1.0/dashboard', methods=['GET'])
def dashboard():
    return jsonify("Dashboard")


@app.route('/api/v1.0/scraper', methods=['GET'])
def scraper():
    # get scrapper list
    # Create new scrapper
    return jsonify('scraper! List')


@app.route('/api/v1.0/jobs', methods=['GET'])
def jobs():
    return jsonify('jobs!')
#
#
@app.route('/api/v1.0/data/<_id>', methods=['GET'])
def data(_id):
    return jsonify(f'data!{_id}')


if __name__ == '__main__':
    app.run()
