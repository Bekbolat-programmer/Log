from flask import Flask, render_template

ap = Flask(__name__)


@ap.route('/training/<prof>')
def index(prof):
    return render_template('training.html', prof=prof.lower())


if __name__ == '__main__':
    ap.run(port=8080, host='127.0.0.1')