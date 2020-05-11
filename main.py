from flask import Flask, render_template, request, redirect, url_for, make_response
import random
import datetime

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")


@app.route("/fakebook")
def fakebook():
    return render_template("fakebook.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/lucky_number", methods=['GET', 'POST'])
def lucky_number():

    if request.method == "GET":
        secret_number = random.randint(1, 10)

        context = {
            "date_of_number": datetime.datetime.now().isoformat(),
            "lucky_number": secret_number
        }

        response = make_response(render_template("lucky_number.html", **context))
        response.set_cookie("lucky_number/secret", secret_number)

        return

    elif request.method == "POST":
        user_guess = request.form.get('number')
        user_secret_cookie = request.cookies.get("lucky_number/secret")
        if user_guess == user_secret_cookie:
            print("User succeeded in guessing")
            return
        else:
            print("user guessed wrong: ", user_guess, "but secret number was: ", user_secret_cookie)
        return redirect(url_for('lucky_number'))

@app.route("/lucky_number/succeess", methods=["GET"])
def lucky_number_success():
    return render_template("lucky_number_success.html")


# TODO1: add boogle site
# TODO2: add hairdresser site

@app.route("/friseur")
def friseur():
    return render_template("friseurindex.html")


if __name__ == '__main__':
    app.run()
