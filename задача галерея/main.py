from flask import Flask, request, render_template
import os
enctype = "multipart/form-data"

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/galery', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        data = os.listdir('static/img')
        data2 = []
        for i in data:
            data2.append('static/img/' + i)
        data = data2
        return render_template('css/index.html', data=data)
    elif request.method == 'POST':
        for i in range(1000):
            if not os.path.exists('static/img/r' + str(i) + '.png'):
                chislo = i
                f = request.files['file']
                f.save('static/img/r' + str(chislo) + '.png')
                break
        data = os.listdir('static/img')
        data2 = []
        for ii in data:
            data2.append('static/img/' + ii)
        data = data2
        # with open('static/img/riana.png', 'wb') as ff:
        # ff.write(f.read())
        return render_template('css/index.html', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    