# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask

app = Flask(__name__)


# Flask中参数表示模板或包的名称,python会根据所处的模板赋予特殊变量__name__相应的值
# 帮助Flask在相应的文件夹里找到需要的资源，比如模板和静态文件。


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command 注册一个flaks命令
@app.cli.command()
# 在命令行中使用 flask hello 
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')



