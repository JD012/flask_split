'''
面向切面编程
中间件
两个概念：切点和切面
      切点：可以在那切开
      切面：从切点处切开能获得什么
flask内置对象：g
      g:可以跨函数使用，将数据传到App/views/permission_book.py
缓存
token

'''
from flask import request, g

from App.extension import cache
from App.models import Student

require_login_list = ["/books/",]


def load_middleware(app):

    @app.before_request
    def before_request():
        path = request.path
        if path in require_login_list:
            token = request.args.get("token")

            if not token:
                return "token 不存在"

            student_id = cache.get(token)

            if not student_id:
                return "id 已过期"

            student = Student.query.get(student_id)

            if not student:
                return "student 已消失"

            g.user = student
            g.auth = token