from flask import Flask, url_for, request
import os

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def empty():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for("static", filename="css/form.css")}"/>
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1 class=text-center>Загрузка фотографии</h1>
                                <h2 class=text-center>Для участия в мисссии</h2>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        {f'<img src="{url_for("static", filename="img/image.jpg")}">' * os.path.exists('static/img/image.jpg')}
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        if not os.path.exists('static/img'):
            os.mkdir('static/img')
        with open('static/img/image.jpg', 'wb') as file:
            file.write(request.files['file'].read())
        return ''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')