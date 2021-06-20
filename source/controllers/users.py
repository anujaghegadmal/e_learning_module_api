from source import app, token_authenticator, token_data, roles
from flask import request, make_response
from source.models.users_model import users_model
from flask_cors import CORS,cross_origin

obj=users_model()

@app.route("/users/login_in",methods=["POST"])
@cross_origin()
def login_in():
    try:
        data=request.form.to_dict()
        print(data)
        return make_response(obj.login_in_model(data))
        
    except Exception as e:
        print(e)
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/login_std",methods=["POST"])
@cross_origin()
def login_std():
    try:
        data=request.form.to_dict()
        print(data)
        return make_response(obj.login_std_model(data))
        
    except Exception as e:
        print(e)
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/create",methods=["POST"])
@cross_origin()
def add_user():
    try:
        # Getting values sent from postman in request.form
        # Converting Key values in dictionary using to_dict()
        data=request.form.to_dict()
        return obj.add_user_model(data)
        
    except Exception as e:
        print(e)
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/read")
@cross_origin()
def list_user():
    try:
        return obj.list_user_model()

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/update",methods=["POST"])
@cross_origin()
@token_authenticator(roles["everyone"])
def update_user():
    try:
        data=request.form.to_dict()
        print(token_data["data"]["id"])
        return obj.update_user_model(data,token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/delete")
@cross_origin()
@token_authenticator(roles["everyone"])
def delete_user():
    try:
        print(token_data["data"]["id"])
        return obj.delete_user_model(token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/get_single_user_details")
@cross_origin()
@token_authenticator(roles["everyone"])
def single_user_details():
    try:
        print(token_data["data"]["id"])
        return obj.single_user_details_model(token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)