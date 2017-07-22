from flask import Flask
from flask import request
from flask import abort
from flask import make_response
from flask.ext.script import Manager

app = Flask(__name__)

# 定义路由，使用装饰器把函数注册为路由，index()函数也是根地址的处理程序
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your Browser is %s.</p>' % user_agent
    # return '<h1>Bad Request</h1>', 200
    # response = make_response('<h1>This doc carries a cookie!</h1>')
    # response.set_cookie('answer',42)
    # return response

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s! </h1>' % name

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name


if __name__ == '__main__':
    app.run(debug=True)
