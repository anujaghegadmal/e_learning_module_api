from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class videos_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="e_learning",user="postgres",host="localhost",password="123",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_video_model(self,data,course_id,id):
        try:
            print(data)
            self.cursor.execute("insert into videos(video_title,video_description,video_path,video_thumbnail,course_id,created_by,status) values('"+data["video_title"]+"','"+data["video_description"]+"','"+data["video_path"]+"','"+data["video_thumbnail"]+"','"+course_id+"','"+str(id)+"','p')")
            return make_response({"status_message":"VIDEO INSERTED SUCCESSFULLY"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    # 14th call
    def list_video_model(self,id):
        try:
            self.cursor.execute("select * from videos_v where created_by ="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)
 
    # 8th call
    def update_video_model(self,data,video_id,id):
        try:
            self.cursor.execute("update videos set video_title='"+data["video_title"]+"', video_description='"+data["video_description"]+"', video_path='"+data["video_path"]+"', video_thumbnail='"+data["video_thumbnail"]+"', course_id="+data["course_id"]+", created_by="+str(id)+", status='p' where id="+video_id)
            return make_response({"status_message":"VIDEO UPDATED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    # 7th call
    def delete_video_model(self,video_id,id):
        try:
            print(video_id)
            self.cursor.execute("update videos set status='z' where id="+video_id+" and created_by="+str(id))
            return make_response({"status_message":"VIDEO DELETED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)
    
    # 12th call
    def publish_video_model(self,video_id,id):
        try:
            self.cursor.execute("update videos set status='a' where id="+video_id+" and created_by="+str(id))
            return make_response({"status_message":"VIDEO PUBLISHED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    # 13th call
    def get_course_wise_videos_model(self,course_id):
        try:
            # print("select * from videos_v where status='a' and course_id="+course_id)
            self.cursor.execute("select * from videos_v where status='a' and course_id="+course_id)
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    # 15th call
    def get_video_details_model(self,course_id,id):
        try:
            self.cursor.execute("select * from videos_v where status='p' and course_id="+course_id+" and created_by="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def total_videos_model(self,id):
        try:
            self.cursor.execute("select count(id) as video_count from videos_v where created_by="+str(id))
            fetched_data = self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    
    