import mysql.connector
from flask import make_response 
from datetime import datetime,timedelta
import jwt
from config.config import dbconfig

class user_model():
    
    def __init__(self):

        # Connection Establishment Code
        try:
            self.con=mysql.connector.connect(host=dbconfig['hostname'],username=dbconfig['username'],password=dbconfig['password'],database=dbconfig['database'])
            self.con.autocommit=True
            print("**********************Connection Established Successfully**********************")
            self.cur=self.con.cursor(dictionary=True)
            
        except:
            print("**********************Error in Connecting with the Mysql Server**********************")


    def user_getall_model(self):

        self.cur.execute("SELECT * FROM users")
        results=self.cur.fetchall()
        print(f"\nResults: {results}\n")
        if len(results)>0:
            
            res=make_response({"message":"Data Fetched Successfully",'payload':results},200)
            res.headers['Access-Control-Allow-Origin']='*'
            return res
        else:
            return make_response({"message":"NO DATA FOUND"},204)


    def user_addone_model(self,data):

        try:
            print(f"\nInput Data: {data}\n")
            name=data['Name']
            email=data['Email']
            phone_num=data['Phone']
            role_id=data['Role_id']
            password=data['Password']

            self.cur.execute(f"INSERT INTO users(Name,Email,Phone,role_id,Password) VALUES('{name}','{email}','{phone_num}','{role_id}','{password}')")

            return make_response({"message":"User Created Succssfully"},201)
        
        except Exception as error:
            print(f"Error: {error}")
            return make_response({"message":"Unable to Create a User"},204)


    def user_update_model(self,data):

        try:
            print(f"\nInput Data: {data}\n")
            id=data['id']
            name=data['Name']
            email=data['Email']
            phone_num=data['Phone']
            role_id=data['Role_id']
            password=data['Password']

            self.cur.execute(f"UPDATE users SET Name='{name}',Email='{email}',Phone='{phone_num}',role_id='{role_id}',Password='{password}' WHERE id={id}")
            
            if self.cur.rowcount>0:
                return make_response({"message":"User Updated Succssfully"},201)
            else:
                return make_response({"message":"Nothing to Update"},202)
        
        except Exception as error:
            print(f"Error: {error}")
            return make_response({"message":"Unable to Update a User"},204)


    def user_delete_model(self,id):
         
        try:
            print(f"\nID: {id}")
            self.cur.execute(f"DELETE FROM users WHERE id={id}")
            
            if self.cur.rowcount>0:
                return make_response({"message":"User Deleted Succssfully"},200)
            else:
                return make_response({"message":"Nothing to Delete"},202)
            
        except Exception as error:
            print(f"Error: {error}")
            return make_response({"message":"Unable to Delete a User"},204)
        

    def user_patch_model(self,id,data):

        try:
            print(f"\nInput Data: {data}\nID:{id}")

            qry = "UPDATE users SET "
            for key,value in data.items():
                qry += f"{key}='{value}',"

            qry=qry[:-1] + f" WHERE id={id}"
            print(f"Query: {qry}")

            self.cur.execute(qry)

            if self.cur.rowcount>0:
                return make_response({"message":"User Updated Succssfully"},201)
            else:
                return make_response({"message":"Nothing to Update"},202)
                    
        except Exception as error:
            print(f"Error: {error}")
            return make_response({"message":"Unable to Update a User"},204)


    def user_pagination_model(self,limit,page):

        start=(page*limit)-limit

        self.cur.execute(f"SELECT * FROM users LIMIT {int(start)}, {int(limit)}")
        results=self.cur.fetchall()
        print(f"\nResults: {results}\n")
        if len(results)>0:
            
            res=make_response({"message":"Data Fetched Successfully",'payload':results,"page_no":page,"limit":limit},200)
            res.headers['Access-Control-Allow-Origin']='*'
            return res
        else:
            return make_response({"message":"NO DATA FOUND"},204)


    def user_update_model(self,data):

        try:
            print(f"\nInput Data: {data}\n")
            id=data['id']
            name=data['Name']
            email=data['Email']
            phone_num=data['Phone']
            role_id=data['Role_id']
            password=data['Password']

            self.cur.execute(f"UPDATE users SET Name='{name}',Email='{email}',Phone='{phone_num}',role_id='{role_id}',Password='{password}' WHERE id={id}")
            
            if self.cur.rowcount>0:
                return make_response({"message":"User Updated Succssfully"},201)
            else:
                return make_response({"message":"Nothing to Update"},202)
        
        except Exception as error:
            print(f"Error: {error}")
            return make_response({"message":"Unable to Update a User"},204)


    def user_upload_avatar_model(self,uid,file):

        try:
            print(f"\nUID : {uid}\nFile: {file}")

            self.cur.execute(f"UPDATE users SET Avatar='{file}' WHERE id={uid}")
            
            if self.cur.rowcount>0:
                return make_response({"message":"File Uploaded Successfully"},201)
            else:
                return make_response({"message":"Nothing to Update"},202)

        except:
            return make_response({"message":"Unable to Upload the File"},204)


    def user_login_model(self,data):

        try:

            print(f"\n\nData: {data}")

            self.cur.execute(f"SELECT ID,Name,Email,Phone,Avatar,role_id FROM users WHERE Email='{data['Email']}' and Password='{data['Password']}'")
            results = self.cur.fetchall()
            userdata = results[0]

            exp_time = datetime.now() + timedelta(minutes=15)
            exp_epoch_time = int(exp_time.timestamp())

            payload={
                "payload": userdata,
                "exp":exp_epoch_time
            }
            
            token = jwt.encode(payload,"yashjain",algorithm="HS256")

            return make_response({'message':"Token Generated Successfully","token":token},200)

        except:
            return make_response({'message':"Invalid Credentials"},401)

