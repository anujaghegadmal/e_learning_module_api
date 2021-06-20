from source import app, token_authenticator, token_data, roles
from flask import request,make_response
from source.models.enrollments_model import enrollments_model
from flask_cors import CORS,cross_origin

obj=enrollments_model()

@app.route("/enrollments/create",methods=["POST"])
@cross_origin()
@token_authenticator(roles["std_only"])
def add_enrollment():
    try:
        data=request.form.to_dict()
        print(token_data["data"]["id"])
        return obj.add_enrollment_model(data,token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/read")
@cross_origin()
@token_authenticator(roles["std_only"])
def list_enrollment():
    try:
        print(token_data["data"]["id"])
        return obj.list_enrollment_model(token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/read_in")
@cross_origin()
@token_authenticator(roles["in_only"])
def list_enrollment_in():
    try:
        print(token_data["data"]["id"])
        return obj.list_enrollment_in_model(token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/update/<enrollments_id>")
@cross_origin()
@token_authenticator(roles["std_only"])
def update_enrollment(enrollments_id):
    try:
        print(token_data["data"]["id"])
        return obj.update_enrollment_model(enrollments_id,token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/show_fav")
@cross_origin()
@token_authenticator(roles["std_only"])
def list_fav_courses():
    try:
        print(token_data["data"]["id"])
        return obj.list_fav_courses_model(token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)


# @app.route("/enrollments/delete/<id>")
# @cross_origin()
# def delete_enrollment(id):
#     try:
#         return obj.delete_enrollment_model(id)

#     except Exception as e:
#             return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/my_enrollments")
@cross_origin()
@token_authenticator(roles["std_only"])
def my_enrollments():
    try:
        print(token_data["data"]["id"])
        return obj.my_enrollments_model(token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/total_enrollments")
@cross_origin()
@token_authenticator(roles["in_only"])
def total_enrollments():
    try:
        print(token_data["data"]["id"])
        return obj.total_enrollments_model(token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)
