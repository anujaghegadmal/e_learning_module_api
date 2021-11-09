from source import app, token_authenticator, token_data, roles
from flask import request, make_response, send_file
from source.models.courses_model import courses_model
from flask_cors import CORS,cross_origin
import os
import time

obj=courses_model()
# print(app.root_path)
@app.route("/courses/create",methods=["POST"])
@cross_origin()
@token_authenticator(roles["in_only"])
def add_course(): 
    try:
        data=request.form.to_dict()
        print(data)
        # print(token_data["data"]["id"])
        # return make_response({"success":"This is add course function"})
        return obj.add_course_model(data,token_data["data"]["id"])

    except Exception as e:
        print(e)
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/read")
@cross_origin()
def list_course():
    try:
        return obj.list_course_model()

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/active_courses")
@cross_origin()
@token_authenticator(roles["in_only"])
def list_course_in():
    try:
        print(token_data["data"]["id"])
        return obj.list_course_in_model(token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/read/<course_id>")
@cross_origin()
@token_authenticator(roles["in_only"])
def single_course(course_id):
    try:
        print(token_data["data"]["id"])
        return obj.single_course_model(course_id,token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)


@app.route("/courses/pending_courses")
@cross_origin()
@token_authenticator(roles["in_only"])
def list_pending_course():
    try:
        print(token_data["data"]["id"])
        return obj.list_pending_courses_model(token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/update/<course_id>",methods=["POST"])
@cross_origin()
@token_authenticator(roles["in_only"])
def update_course(course_id):
    try:
        data=request.form.to_dict()
        print(token_data["data"]["id"])
        return obj.update_course_model(data,course_id,token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/delete/<course_id>")
@cross_origin()
@token_authenticator(roles["in_only"])
def delete_course(course_id):
    try:
        print(token_data["data"]["id"])
        return obj.delete_course_model(course_id,token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/deleted_courses")
@cross_origin()
@token_authenticator(roles["in_only"])
def list_deleted_courses():
    try:
        data=request.form.to_dict()
        print(token_data["data"]["id"])
        return obj.list_deleted_courses_model(data,token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/delete_permanently/<course_id>")
@cross_origin()
@token_authenticator(roles["in_only"])
def delete_permanently(course_id):
    try:
        print(token_data["data"]["id"])
        return obj.delete_permanently_model(course_id,token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/list_all_courses")
@cross_origin()
@token_authenticator(roles["in_only"])
def list_all_courses():
    try:
        print(token_data["data"]["id"])
        return obj.list_all_courses_model(token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/search_course/<search>")
@cross_origin()
def search_course(search):
    try:
        return obj.search_course_model(search)

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/publish_course/<course_id>")
@cross_origin()
@token_authenticator(roles["in_only"])
def publish_course(course_id):
    try:
        print(token_data["data"]["id"])
        return obj.publish_course_model(course_id,token_data["data"]["id"])

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/upload_thumbnail", methods=["POST"])
@cross_origin()
# @token_authenticator(roles["in_only"])
def upload_thumbnail():
    file=request.files['file']
    current_time=str(time.time())
    time_frags=current_time.split(".")
    final_filename=time_frags[0]+time_frags[1]+os.path.splitext(file.filename)[1]
    # print(os.path.splitext(file.filename))
    # print(os.path.splitext(file.filename)[1])
    file.save(os.path.join(app.root_path+"/uploads/",final_filename))
    # print(file.filename)
    return make_response({"filename":"uploads/"+final_filename},200)

@app.route("/uploads/<filename>")
@cross_origin()
def list_uploads(filename):
    return send_file(app.root_path+"/uploads/"+filename)

@app.route("/courses/total_courses")
@cross_origin()
@token_authenticator(roles["in_only"])
def total_courses():
    try:
        print(token_data["data"]["id"])
        return obj.total_courses_model(token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)
