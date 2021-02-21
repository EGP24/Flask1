from flask import Flask

app = Flask(__name__)
description = {'Меркурий': ['Самая близкая к Солнцу планета', 'Самая маленькая планета Солнечной системы',
                            'Напоминает Луну по своим физическим характеристикам', 'Есть скопления льда на полюсах'],
               'Венера': ['Третий по яркости объект на Земном небе', 'По составу напоминает Землю',
                          'Атмосфера состоит из углекислого газа', 'Постоянно идут кислотные дожди'],
               'Марс': ['Много необходимых ресурсов', 'Есть вода и атмосфера', 'Есть небольшое магнитное поле',
                        'Просто красивая'],
               'Юпитер': ['Самая большая планета Солнечной системы', 'Самая быстро вращающаяся планета в Солнечной системе',
                          'Самое мощное магнитное поле в Солнечной системе', 'Имеет спутник, который больше Меркурия)'],
               'Сатурн': ['Наименее плотная планета Солнечной системы', 'Не имеет твёрдой поверхности',
                          'Имеет спутник, который больше Меркурия))', 'Сутки длятся 10 Земных часов'],
               'Уран': ['Самая холодная планета', 'Можно уыидеть невооружённым глазом с Земли',
                        'Сутки длятся 17 Земных часов', 'Просто ражачная планета))'],
               'Нептун': ['Самая далёкая планета от Солнца', 'Имеет небольшое магнитное поле',
                          'Синего цвета, хотя и не известно почему', 'Самый маленький гигант']}
params = ['class="alert alert-success"', 'class="alert alert-dark"',
          'class="alert alert-warning"', 'class="alert alert-danger"']


@app.route('/choice/<planet_name>')
def empty(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}</h1>
                    {chr(10).join([f"<h3 {j}>{i}</h3>" for i, j in zip(description[planet_name], params)])}
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')