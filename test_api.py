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
    
==========
     
class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userName = args['user_name']
            _userPassword = args['password']
            return {'Email': args['email'], 'UserName': args['user_name'], 'Password': args['password']}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateUser, '/user')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="4723")
