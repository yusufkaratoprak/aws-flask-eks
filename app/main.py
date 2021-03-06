import platform
from flask import Flask
from flask_restplus import Resource, Api
app = Flask(__name__)
api = Api(app)
@api.route('/uname')
class HostName(Resource):
    def get(self):
        return {'uname': platform.uname()}
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)