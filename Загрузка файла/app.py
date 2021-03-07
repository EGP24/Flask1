from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def empty():
    if not os.path.exists('static/img'):
        os.mkdir('static/img')
    if request.method == 'POST':
        with open('static/img/image.jpg', 'wb') as file:
            file.write(request.files['file'].read())
    return render_template('login.html', flag=os.path.exists('static/img/image.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')