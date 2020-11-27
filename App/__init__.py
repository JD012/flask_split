from flask import Flask

from App.extension import init_ext
from App.middleware import load_middleware
from App.settings import envs
from App.views import init_blue


def create_app(env):
    app = Flask(__name__)

    # 初始化App的配置
    app.config.from_object(envs.get(env))

    # 初始化第三方的插件
    init_ext(app=app)

    # 加载中间件
    load_middleware(app=app)

    # 初始化路由系统
    init_blue(app=app)

    return app