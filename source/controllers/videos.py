from source import app,token_authenticator, token_data, roles
from flask import request, make_response, send_file
from source.models.videos_model import videos_model
from flask_cors import CORS,cross_origin
# import ffmpeg_streaming
# from ffmpeg_streaming import Formats
import os
import time


obj=videos_model()

@app.route("/videos/create/<course_id>",methods=["POST"])
@cross_origin()
@token_authenticator(roles["in_only"])
def add_video(course_id):
    try:
        data=request.form.to_dict()
        print(token_data["data"]["id"])
        return obj.add_video_model(data,course_id,token_data["data"]["id"])
        # return "hgdf"
    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/read")
@cross_origin()
@token_authenticator(roles["in_only"])
def list_video():
    try:
        print(token_data["data"]["id"])
        return obj.list_video_model(token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/update/<video_id>",methods=["POST"])
@cross_origin()
@token_authenticator(roles["in_only"])
def update_video(video_id):
    try:
        data=request.form.to_dict()
        print(data)
        print(token_data["data"]["id"])
        return obj.update_video_model(data,video_id,token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/delete/<video_id>")
@cross_origin()
@token_authenticator(roles["in_only"])
def delete_video(video_id):
    try:
        print(token_data["data"]["id"])
        return obj.delete_video_model(video_id,token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/publish_video/<video_id>")
@cross_origin()
@token_authenticator(roles["in_only"])
def publish_video(video_id):
    try:
        print(token_data["data"]["id"])
        return obj.publish_video_model(video_id,token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/course_videos/<course_id>")
@cross_origin()
@token_authenticator(roles["everyone"])
def get_course_wise_videos(course_id):
    try:
        return obj.get_course_wise_videos_model(course_id)

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/video_details/<course_id>")
@cross_origin()
@token_authenticator(roles["in_only"])
def get_video_details(course_id):
    try:
        print(token_data["data"]["id"])
        return obj.get_video_details_model(course_id,token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/upload_vdo/<course_id>", methods=["POST"])
@cross_origin()
@token_authenticator(roles["in_only"])
def upload_vdo(course_id):
    try:
        file = request.files['file']
        current_time = str(time.time())
        time_frags = current_time.split(".")
        final_filename = time_frags[0]+time_frags[1]+os.path.splitext(file.filename)[1]
        # print(time_frags[0])
        # print(time_frags[1])
        # print(os.path.splitext(file.filename)[1])
        # print(final_filename)
        video_path = "/uploads_v/"+str(token_data["data"]["id"])+"/"+str(course_id)+"/"+str(time_frags[0])
        os.mkdir(app.root_path+video_path)
        file.save(os.path.join(app.root_path+video_path, final_filename))
        save_to = app.root_path+"/uploads_v/"+str(token_data["data"]["id"])+"/"+str(course_id)
        url = app.root_path+"/uploads_v/"+str(token_data["data"]["id"])+"/"+str(course_id)
        video = ffmpeg_streaming.input(os.path.join(app.root_path+video_path, final_filename))
        # print(video)
        hls = video.hls(Formats.h264())
        # print(hls)
        hls.encryption(save_to, url)
        hls.auto_generate_representations()
        hls.output(video_path+"/hls.m3u8")
        # print(hls.output(video_path+"/hls.m3u8"))
        # print(video_path+os.path.splitext(file.filename)[1])
        return make_response({"filename":video_path+"/hls.m3u8"},200)
    
    except Exception as e:
        print(str(e))
        return make_response({"Error":str(e)},500)

@app.route("/videos/uploads_v/<filename>")
@cross_origin()
def list_uploads_v(filename):
    return send_file(app.root_path+"/uploads_v/"+filename)

@app.route("/videos/total_videos")
@cross_origin()
@token_authenticator(roles["in_only"])
def total_videos():
    try:
        print(token_data["data"]["id"])
        return obj.total_videos_model(token_data["data"]["id"])

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)
