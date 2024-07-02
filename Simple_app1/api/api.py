
from flask import Flask, jsonify, request 
from flask_restful import Api
from routes import Routes

app = Flask(__name__) 

print('__name__ is {0}'.format(__name__))

if __name__ in ['__main__', 'api']:
    
    route = Routes(app=app, base_path='/api/v1')
    upload = app.config['image']
    app.run(debug=True)
