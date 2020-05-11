import uuid
​
from flask import Flask, render_template, request, redirect, url_for, make_response
import random
import datetime
from models import User, SecretNumberStore, db
​
app = Flask(__name__)
db.create_all()


COOKIE_ID_STRING = "lucky_number/secret_number_identifier"
​

@app.route("/")
def main():
    return render_template("main.html")
​
​
@app.route("/fakebook")
def fakebook():
    return render_template("fakebook.html")
​
​
@app.route("/about")
def about():
    return render_template("about.html")
​
​
@app.route("/lucky_number", methods=['GET', 'POST'])
def lucky_number():
    if request.method == "GET":
​
        secret_number_identifier = request.cookies.get("lucky_number/secret_number_identifier")
        secret_number_store = db.query(SecretNumberStore).filter_by(cookie_identifier=secret_number_identifier).first()
​
        if not secret_number_store:
            secret_number = random.randint(1, 10)
            cookie_identifier = str(uuid.uuid4())
            secret_number_store = SecretNumberStore(
                cookie_identifier=cookie_identifier,
                secret_number=secret_number
            )
            db.add(secret_number_store)
            db.commit()
​
        context = {
            "date_of_number": datetime.datetime.now().isoformat(),
        }
​
        response = make_response(render_template("lucky_number.html", **context))
        response.set_cookie("lucky_number/secret_number_identifier", str(secret_number_store.cookie_identifier))
        return response
​
    elif request.method == "POST":
        user_guess = request.form.get('number')
        secret_number_identifier = request.cookies.get("lucky_number/secret_number_identifier")
​
        secret_number_store = db.query(SecretNumberStore).filter_by(cookie_identifier=secret_number_identifier).first()
        print("user guess:", user_guess)
        print("secret_number_identifier:", secret_number_identifier)
        print("secret_number:", secret_number_store.secret_number)
        if secret_number_store and (int(user_guess) == secret_number_store.secret_number):
            response = make_response(redirect(url_for('lucky_number_success')))
            response.set_cookie("lucky_number/secret_number_identifier", expires=0)
​
            db.delete(secret_number_store)
            db.commit()
            return response
        else:
            return redirect(url_for('lucky_number'))
​
​
@app.route("/lucky_number/success", methods=["GET"])
def lucky_number_success():
    return render_template("lucky_number_success.html")
​
​
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        users = db.query(User).all()
        context = {
            "users": users
        }
        return render_template("register.html", **context)
    elif request.method == "POST":
        username = request.form.get("username")
        new_user = User(name=username, secret_number=10)
        db.add(new_user)
        db.commit()                                             # abspeichern aller geaddeten elemente, in einer transaktion.
        return redirect(url_for('register'))
​
​
# TODO TODAY:
# - Post Form finish, get input parameters from request
# - Cookies
# - Database
​
​
# TODO: 1) add boogle site
# TODO: 2) add hair dresser site
​
​
if __name__ == '__main__':
    app.run(debug=True)


