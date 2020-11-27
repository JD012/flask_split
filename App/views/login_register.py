'''
uuid生成token唯一值
缓存：对token进行过期时间设置
abort
'''
import uuid

from flask import Blueprint, request, abort, jsonify

from App.extension import cache
from App.models import Student

blue_student = Blueprint("blue_student", __name__, url_prefix='/students')


@blue_student.route("/", methods=["POST", ])
def students():
    action = request.args.get("action")

    username = request.form.get("username")
    password = request.form.get("password")

    if action == "register":

        student = Student()
        student.s_name = username
        student.s_password = password

        if not student.save():
            abort(401)
        return "注册成功"

    elif action == "login":

        # Student.query.filter(Student.s_name.__eq__(username))
        student_list = Student.query.filter(Student.s_name == (username)).all()
        if not student_list:
            abort(404)
        student = student_list[0]

        if not student.verify_password(password):
            abort(401)

        token = uuid.uuid4().hex

        cache.set(token, student.id, timeout=60*60*24)

        data = {
            "msg": "登录成功",
            "token": token
        }

        return jsonify(data)

    else:
        abort(400)
