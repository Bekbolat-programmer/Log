from flask import Flask, render_template

ap = Flask(__name__)


@ap.route('/<title>')
@ap.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    ap.run(port=8080, host='127.0.0.1')