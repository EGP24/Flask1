from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def empty():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>На учатие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="firstname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="firstname">
                                    <input type="text" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите имя" name="name">
                                    </br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Его нет</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Начальное</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession1" name="profession">
                                          <label class="form-check-label" for="profession1">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession2" name="profession">
                                          <label class="form-check-label" for="profession2">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession3" name="profession">
                                          <label class="form-check-label" for="profession3">Строитель</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession4" name="profession">
                                          <label class="form-check-label" for="profession4">Экзобиолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession5" name="profession">
                                          <label class="form-check-label" for="profession5">Врач</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession6" name="profession">
                                          <label class="form-check-label" for="profession6">Климатолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession7" name="profession">
                                          <label class="form-check-label" for="profession7">Астрогеолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="profession8" name="profession">
                                          <label class="form-check-label" for="profession8">Оператор марсохода</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">Мужской</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">Женский</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли вы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')