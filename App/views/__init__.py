from App.views.book_blue import book_blue
from App.views.first_blue import blue
from App.views.student_blue import blue_student


def init_blue(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=blue_student)
    app.register_blueprint(blueprint=book_blue)