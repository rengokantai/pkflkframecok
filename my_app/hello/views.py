__author__ = 'Hernan Y.Ke'
from flask import render_template, request

@hello.route('/')
@hello.route('/hello')
def hello():
    user = request.args.get('user', 'Shalabh')
    return render_template('index.html', user=user)