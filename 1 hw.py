from flask import Flask, render_template, redirect

ap = Flask(__name__)


@ap.route('/distribution')
def distribution():
    astr = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                  'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', astr=astr)


@ap.route('/')
def index():
    return redirect('/distribution')


if __name__ == '__main__':
    ap.run(port=8080, host='127.0.0.1')