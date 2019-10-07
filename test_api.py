from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import request, jsonify
from date import datetime

app = Flask(__name__)
api = Api(app)
@class app
class RegistUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        args = parser.parse_args()

        name = args['name']
        email = args['email']

        return {'name': name, 'email': email}
     def test_script(self):
         

api.add_resource(RegistUser, '/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
===============

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['myName']
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('myName')
      return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=
