from flask import Flask, render_template, session, url_for, redirect
from flask_bootstrap import Bootstrap
# from flask.ext.script import Manager
from flask_wtf import FlaskForm
from flask_moment import Moment
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import url_for
from datetime import datetime
import jinja2
from flask import request
from flask import abort
from flask import make_response


app = Flask(__name__)
app.config['SECRET_KEY'] = '@!*H(NF(_S!L'
# manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

# -*- NameForm表单中有一个名为name的文本字段，以及一个名为submit的提交按钮
class NameForm(FlaskForm):

    name = StringField('What is your name?', validators=[DataRequired()]) # StringField类 表示属性为type='text'的<input>元素
    submit = SubmitField('Submit') # SubmitField类 表示属性为type='submit'的<input>元素

# -*- 定义路由，使用装饰器把函数注册为路由，index()函数也是根地址的处理程序
# -*- Flask在URL映射中把这个视图函数注册为GET和POST请求的处理程序。如果没指定methods，就只把它注册为GET请求的处理程序。
@app.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    form = NameForm()

    if form.validate_on_submit():
        session['name'] = form.name.data # session['name']存储了同一个会话中的文本框内容
        form.name.data = ''
        # name = form.name.data
        return redirect(url_for('index'))

    # 使用get()获取字典中键对应的值以避免未找到键的异常情况，因为对于不存在的键，get()会返回None
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))

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
