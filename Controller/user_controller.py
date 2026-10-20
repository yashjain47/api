import datetime
from app import app
from model.user_model import user_model
from model.auth_mode import auth_model
from flask import request,send_file
obj=user_model()
auth=auth_model()

@app.route("/user/getall",methods=["GET"])
@auth.token_auth()
def user_getall_controller():
    return obj.user_getall_model()


@app.route("/user/addone",methods=["POST"])
@auth.token_auth()
def user_addone_controller():
    data=request.form
    return obj.user_addone_model(data)


@app.route("/user/update",methods=["PUT"])
@auth.token_auth()
def user_update_controller():
    data=request.form
    return obj.user_update_model(data)


@app.route("/user/delete/<int:id>",methods=["DELETE"])
@auth.token_auth()
def user_delete_controller(id):
    return obj.user_delete_model(id)


@app.route("/user/patch/<int:id>",methods=["PATCH"])
def user_patch_controller(id):
    data=request.form
    return obj.user_patch_model(id,data)


@app.route("/user/getall/limit/<int:limit>/page/<int:page>",methods=["GET"])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit,page)


@app.route("/user/<int:uid>/upload/avatar",methods=["PUT"])
def user_upload_avatar_controller(uid):
    
    file=request.files['Avatar']
    uniqueFileName = str(datetime.datetime.now().timestamp()).replace(".","")
    filenamesplit = file.filename.split(".")
    ext = filenamesplit[len(filenamesplit)-1]
    finalfilepath = f"uploads/{uniqueFileName}.{ext}"
    file.save(finalfilepath)

    return obj.user_upload_avatar_model(uid,finalfilepath)


@app.route("/uploads/<filename>")
def usr_getavatar_controller(filename):
    return send_file(f"uploads/{filename}")


@app.route("/user/login",methods=["POST"])
def usr_login_controller():
    return obj.user_login_model(request.form)


