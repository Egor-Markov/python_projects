# Импорт
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


def result_calculate(size, lights, device):
    # Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + device * devices_coef


# Первая страница
@app.route("/")
def index():
    return render_template("index.html")


# Вторая страница
@app.route("/<size>")
def lights(size):
    return render_template("lights.html", size=size)


# Третья страница
@app.route("/<size>/<lights>")
def electronics(size, lights):
    return render_template("electronics.html", size=size, lights=lights)


# Расчет
@app.route("/<size>/<lights>/<device>")
def end(size, lights, device):
    return render_template(
        "end.html", result=result_calculate(int(size), int(lights), int(device))
    )


# Форма
@app.route("/form")
def form():
    return render_template("form.html")


# Результаты формы
@app.route("/submit", methods=["POST"])
def submit_form():
    # Создай переменные для сбора информации
    name = request.form["name"]
    email = request.form["email"]
    address = request.form["address"]
    date = request.form["date"]
    print(f"Name:{name}")
    print(f"Email:{email}")
    print(f"Address:{address}")
    print(f"Date:{date}")

    with open("form.txt", "a", encoding="UTF-8") as f:
        f.write(name + "\n")  # Переменная + '\n'

    with open("form.txt", "a", encoding="UTF-8") as f:
        f.write(email + "\n")

    with open("form.txt", "a", encoding="UTF-8") as f:
        f.write(address + "\n")

    with open("form.txt", "a", encoding="UTF-8") as f:
        f.write(date + "\n")

    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template(
        "form_result.html",
        # Помести переменные
        name=name,
        email=email,
        address=address,
        date=date,
    )


def new_func():
    address = request.form["address"]
    return address


#
#
##
#
##
#
#
#
#
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///diary.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Создание db
db = SQLAlchemy(app)
# Создание таблицы


class Card(db.Model):
    # Создание полей
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Заголовок
    title = db.Column(db.String(100), nullable=False)
    # Описание
    subtitle = db.Column(db.String(300), nullable=False)
    # Текст
    text = db.Column(db.Text, nullable=False)

    # Вывод объекта и id
    def __repr__(self):
        return f"<Card {self.id}>"


app.run(debug=True)
