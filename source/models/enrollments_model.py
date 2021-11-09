from flask import make_response
import psycopg2
from psycopg2.extras import RealDictCursor

class enrollments_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="e_learning",user="postgres",host="localhost",password="123",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def add_enrollment_model(self,data,id):
        try:
            print(data)
            # print(data["course_id"])
            self.cursor.execute("insert into enrollments(created_by,course_id,status) values("+str(id)+",'"+data["course_id"]+"','a')")
            return make_response({"status_message":"ENROLLED SUCCESSFULLY"},200)

        except Exception as e:
            print(str(e))
            return make_response({"Error":str(e)},500)


    def add_favourites_model(self,data,id):
        try:
            print(data)
            # print(data["course_id"])
            self.cursor.execute("insert into enrollments(created_by,course_id,status) values("+str(id)+",'"+data["course_id"]+"','f')")
            return make_response({"status_message":"COURSE ADDED TO FAVOURITES"},200)

        except Exception as e:
            print(str(e))
            return make_response({"Error":str(e)},500)


    def list_enrollment_model(self,id):
        try:
            self.cursor.execute("select * from enrollments where status='f' and created_by="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def list_enrollment_in_model(self,id):
        try:
            self.cursor.execute("select * from my_enrollments_instructor_v where status='a' and instructor_id="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)


    def update_enrollment_model(self,enrollments_id,id):
        try:
            self.cursor.execute("update enrollments set status='a' where id="+enrollments_id+" and created_by="+str(id))
            return make_response({"status_message":"ENROLLMENT UPDATED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    # def delete_enrollment_model(self,id):
    #     try:
    #         return make_response({"status_message":"ENROLLMENT DELETED SUCCESSFULLY"},200)

    #     except Exception as e:
    #         return make_response({"Error":str(e)},500)

    def my_enrollments_model(self,id):
        try:
            self.cursor.execute("select * from my_enrollments_v where status='a' and student_id="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def list_fav_courses_model(self,id):
        try:
            # list all favourite courses 
            self.cursor.execute("select * from my_enrollments_v where status='f' and student_id="+str(id))
            # how to add 2 conditions in select query?
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def total_enrollments_model(self,id):
            try:
                self.cursor.execute("select count(student_id) as enrollment_count from my_enrollments_instructor_v where instructor_id="+str(id))
                fetched_data = self.cursor.fetchall()
                print(fetched_data)
                return make_response({"payload":fetched_data},200)

            except Exception as e:
                return make_response({"Error":str(e)},500)