from flask import make_response
import psycopg2 
from psycopg2.extras import RealDictCursor
import jwt
import datetime

class users_model:
    def __init__(self):
        self.con=psycopg2.connect(dbname="e_learning",user="postgres",host="localhost",password="anujagr98",port=5432)
        self.con.set_session(autocommit=True)
        self.cursor=self.con.cursor(cursor_factory=RealDictCursor)

    def login_in_model(self,data):
        try:
            self.cursor.execute("select id, name, role, status from users_v where email='"+data["email"]+"' and password='"+data["password"]+"' and role ='in'")
            fetched_data=self.cursor.fetchall()
            if len(fetched_data)>0:
                print(fetched_data)
                token =jwt.encode({"data":fetched_data,"exp":datetime.datetime.utcnow()+datetime.timedelta(days=100)},"EncryptionKey")
                return make_response({"payload":token},200)
            else:
                return make_response({"Error":"Please check ID or PASSWORD"},403)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def login_std_model(self,data):
        try:
            self.cursor.execute("select id, name, role, status from users_v where email='"+data["email"]+"' and password='"+data["password"]+"' and role ='std'")
            fetched_data=self.cursor.fetchall()
            if len(fetched_data)>0:
                print(fetched_data)
                token =jwt.encode({"data":fetched_data,"exp":datetime.datetime.utcnow()+datetime.timedelta(days=100)},"EncryptionKey")
                return make_response({"payload":token},200)
            else:
                return make_response({"Error":"Please check ID or PASSWORD"},403)

        except Exception as e:
            return make_response({"Error":str(e)},500)


    def add_user_model(self,data):
        try:
            self.cursor.execute("insert into users(name,email,phone_no,password,role,status,img_path) values('"+data["name"]+"','"+data["email"]+"','"+data["phone_no"]+"','"+data["password"]+"','"+data["role"]+"','a','"+data["img_path"]+"')")
            return make_response({"status_message":"USER CREATED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def list_user_model(self):
        try:
            self.cursor.execute("select * from users_v")
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"status_message":"EXECUTED","payload":fetched_data},200)
        
        except Exception as e:
            return make_response({"Error":str(e)},500)

    def update_user_model(self,data,id):
        try:
            print(data)
            self.cursor.execute("update users set name='"+data["name"]+"', email='"+data["email"]+"', phone_no="+data["phone_no"]+", password='"+data["password"]+"', role='"+data["role"]+"', img_path='"+data["img_path"]+"', status='a' where id="+str(id))
            return make_response({"status_message":"USER UPDATED"},200)

        except Exception as e:
            return make_response({"Error":str(e)},500)

    def delete_user_model(self,id):
        try:
            # update query to update status=d
            self.cursor.execute("update users set status='d' where id="+str(id))
            return make_response({"status_message":"USER DELETED"},200)
        
        except Exception as e:
            return make_response({"Error":str(e)},500)

    # 2nd call
    def single_user_details_model(self,id):
        try:
            self.cursor.execute("select * from users_v where id="+str(id))
            fetched_data=self.cursor.fetchall()
            print(fetched_data)
            return make_response({"payload":fetched_data},200)
        
        except Exception as e:
            return make_response({"Error":str(e)},500)