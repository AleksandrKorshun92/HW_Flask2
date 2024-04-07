# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой
# будет создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с
# данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

import json
from flask import Flask, render_template, request, make_response, session, redirect


app = Flask(__name__)
app.secret_key = '123456789'


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        mail = request.form.get("mail")
        if name != None and mail != None:
            context = {'name': name,
                       "mail":mail}
            response = make_response(redirect('/hello/'))
            response.set_cookie('username', context["name"])
            response.set_cookie('mail', context["mail"])
            return response
        else:
            return render_template("404.html")
    return render_template("index_9.html")

@app.route('/getcookie/')
def getcookie():
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"


@app.route('/hello/')
def hello():
    name_user_cookie = request.cookies.get('username')
    mail_user_cookie = request.cookies.get('mail')
    context = {'name': name_user_cookie, 'mail': mail_user_cookie}
    if name_user_cookie and mail_user_cookie:
        with open("user_cookie.json", 'w', encoding='utf-8') as file:
            json.dump(context, file)
        return render_template('hello.html', **context)
    return redirect("/")

@app.route('/delete-cookie/')
def delete_cookie():
    response = make_response(redirect('/'))
    response.set_cookie('username', expires=0)
    response.set_cookie('mail', expires=0)
    return response


if __name__ == "__main__":
    app.run(debug=True)
