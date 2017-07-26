from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from flask.ext.script import Manager
from flask_moment import Moment
from flask import url_for
from datetime import datetime
import jinja2
from flask import request
from flask import abort
from flask import make_response


app = Flask(__name__)
# manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# 定义路由，使用装饰器把函数注册为路由，index()函数也是根地址的处理程序
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
