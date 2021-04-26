from flask import Flask, render_template, redirect

ap = Flask(__name__)


@ap.route('/table/<sex>/<int:age>')
def table_param(a, b):
    return render_template('table.html', a=a, b=b)


@ap.route('/')
def index():
    return redirect('/table/female/12')


if __name__ == '__main__':
    ap.run(port=8080, host='127.0.0.1')