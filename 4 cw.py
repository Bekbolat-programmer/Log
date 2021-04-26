from flask import Flask, render_template

ap = Flask(__name__)


@ap.route('/answer')
@ap.route('/auto_answer')
def auto_answer():
    pr = {}
    pr['title'] = 'Анкета'
    pr['surname'] = 'Watny'
    pr['name'] = 'Mark'
    pr['education'] = 'выше среднего'
    pr['profession'] = 'штурман марсохода'
    pr['sex'] = 'male'
    pr['motivation'] = 'Всегда мечтал застрять на Марсе!'
    pr['ready'] = 'True'
    return render_template('auto_answer.html', **pr)


if __name__ == '__main__':
    ap.run(port=8080, host='127.0.0.1')