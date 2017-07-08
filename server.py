
from flask import Flask,jsonify, request,redirect,url_for,render_template
import requests
import json

import config

app = Flask(__name__)

data_url = None
headers = {
    'Content-Type': 'application/json'
}

"""if config.DEVELOPMENT:"""
if 1==1:
    data_url = 'https://auth.c100.hasura.me'
    headers['Authorization'] = 'Bearer ' + "vx5sbgz4ojabybhbtqi3l9fuioyynq4t"
else:
    # Make a request to the data API as the admin role for full access
    data_url = 'http://data.hasura'
    headers['X-Hasura-Role'] = 'admin'
    headers['X-Hasura-User-Id'] = '1'

query_url = data_url + '/login'

@app.route("/")
def home():
  return "home"

@app.route("/login")
def hello():
    query={"username":"shubhma","password":"WhyShouldItellYou"}
    print("data_url= \n",data_url,"\n","query_url=\n",query_url,"\n headers=\n",headers,"\n data=\n",json.dumps(query))
    r=requests.post(query_url, data=json.dumps(query) ,headers=headers)
    print("r=",r)
    return jsonify(r.json())
    """query ={
            		"type": "select",
            		"args": {
            			"table": "Users",
            			"columns": ["*"]
            			}
            		}

@app.route("/<string:role>")
def get_role(role):
    roles = request.headers['X-Hasura-Allowed-Roles']

    if role in roles:
        return "Hey you have the %s role" % role

    return ('DENIED: Only a user with %s role can access this endpoint' % role, 403)

	
if __name__ == '__main__':
    app.run(debug=True)
