'''
Flask内置对象：g
'''
from flask import Blueprint, request, g

from App.extension import cache
from App.models import Student
from App.models.sutdent_model import PERMISSION_STUDENT_LEARN, PERMISSION_STUDENT_MANAGE

book_blue = Blueprint("book_blue", __name__, url_prefix="/books")


@book_blue.route("/")
def books():

    student = g.user

    if not student.check_permission(PERMISSION_STUDENT_MANAGE):
        return "没有访问本书的权限"

    return "这是你喜欢的书<<算法导论>>，请拿走"
