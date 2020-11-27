'''
知识点：
1.用户密码加密
2.用户密码校验
4.数据自动保存数据库
5.用户权限校验
'''
from werkzeug.security import generate_password_hash, check_password_hash

from App.extension import db

PERMISSION_STUDENT_LEARN = 1
PERMISSION_STUDENT_MANAGE = 2
PERMISSION_STUDENT_USE_PHONE = 4


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16), unique=True)
    _s_password = db.Column(db.String(256))
    s_permission = db.Column(db.Integer, default=PERMISSION_STUDENT_LEARN)

    @property
    def s_password(self):
        raise Exception("can't access")

    @s_password.setter
    def s_password(self, password):
        self._s_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._s_password, password)

    def check_permission(self, permission):
        return self.s_permission & permission == permission

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return True
