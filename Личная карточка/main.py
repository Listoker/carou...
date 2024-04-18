from flask import Flask, url_for
import json
import random

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/member')
def member():
    with open('template/json.json', encoding='UTF-8') as f:
        f = json.load(f)
        kazdoe = []
        for i in f:
            kazdoe.append(i)
        znach = random.choice(kazdoe)
        a = f[znach].split()
        with open(f'{a[3]}', encoding='UTF-8') as ff:
            ff = ff.read()
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>{a[0]} {a[1]}</h1>
                    <img src="{url_for('static', filename=a[2])}" 
           alt="здесь должна была быть картинка, но не нашлась">
           <h3>{ff}</h3>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def cosmos(nickname, level, rating):
    level = str(level)
    rating = str(rating)
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендент на участие в миссии {nickname}:</h2>
                    <div class="alert alert-primary" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-primary" role="alert">
                      составляет {rating}!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')