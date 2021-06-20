from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class courses_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="e_learning",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)
        
    def add_course_model(self,data,id):
        try:
            self.cursor.execute("insert into courses(course_name,course_description,course_img_thumbnail,course_fees,duration,status,created_by) values('"+data["course_name"]+"','"+data["course_description"]+"','"+data["course_img_thumbnail"]+"','"+data["course_fees"]+"','"+data["duration"]+"','p',"+str(id)+")")
            return make_response({"status_message":"COURSE CREATED"},200)
 
        except Exception as e:
            return make_response({"Error":str(e)},500)

    def list_course_model(self):
        try:
            # select all active courses
            self.cursor.execute("select * from courses_v where status='a'")
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def list_course_in_model(self,id):
        try:
            # show all active courses of a current logged in instructor
            self.cursor.execute("select * from courses_v where status='a' and created_by="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def single_course_model(self,course_id,id):
        try:
            # show single course 
            self.cursor.execute("select * from courses_v where status='p' and id="+course_id+" and created_by="+str(id))
            fetched_data=self.cursor.fetchall()
            # print(fetched_data)
            # print("select * from courses_v where status='a' and id="+course_id)
            # print("_______________________")
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)


    def list_pending_courses_model(self,id):
        try:
            # select all pending courses
            self.cursor.execute("select * from courses_v where status='p' and created_by="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data) 
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def update_course_model(self,data,course_id,id):
        try:
            print(data)
            self.cursor.execute("update courses set course_name='"+data["course_name"]+"',course_description='"+data["course_description"]+"',course_img_thumbnail='"+data["course_img_thumbnail"]+"',course_fees="+data["course_fees"]+",duration='"+data["duration"]+"',status='p',created_by="+str(id)+" where id="+course_id)
            return make_response({"status_message":"COURSE UPDATED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    # 11th call
    def delete_course_model(self,course_id,id):
        try:
            # update status to 'd'
            self.cursor.execute("update courses set status='d' where id="+course_id+" and created_by="+str(id))
            return make_response({"status_message":"COURSE DELETED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def list_deleted_courses_model(self,data,id):
        try:
            # list all deleted courses
            self.cursor.execute("select * from courses_v where status='d' and created_by="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def delete_permanently_model(self,course_id,id):
        try:
            # update status to 'z'
            self.cursor.execute("update courses set status='z' where id="+course_id+" and created_by="+str(id))
            return make_response({"status_message":"COURSE DELETED PERMANENTLY"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)


    def list_all_courses_model(self,id):
        try:
            # list all courses irrespective to their status
            self.cursor.execute("select * from courses_v where created_by="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data})

        except Exception as e:
            return make_response({"Error":str(e)},500)

    # 4th call
    def search_course_model(self,search):
        try:
            self.cursor.execute("select * from courses_v where lower(course_name) like '%"+search+"%'")
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"status_message":"COURSE FOUND","payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    # 10th call
    def publish_course_model(self,course_id,id):
        try:
            self.cursor.execute("update courses set status='a' where id="+course_id+" and created_by="+str(id))
            return make_response({"status":"COURSE PUBLISHED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def total_courses_model(self,id):
        try:
            self.cursor.execute("select count(id) as course_count from courses_v where created_by="+str(id))
            fetched_data = self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)
