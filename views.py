from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import sqlite3
import datetime

nw_dt = datetime.datetime.now()
nw_dt = nw_dt.date()
nw_tm = datetime.datetime.now()
nw_tm = nw_tm.time()

views = Blueprint('views', __name__)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember me')


class ChoiceWizard(FlaskForm):
    choice1 = StringField('Interest Category-1', validators=[InputRequired()])
    choice2 = StringField('Interest Category-2', validators=[InputRequired()])
    choice3 = StringField('Interest Category-3', validators=[InputRequired()])


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/choice', methods=['GET', 'POST'])
def choice():
    username = session["username"]
    password = session['password']

    if request.method == 'POST':
        cat1 = request.form['cat-1']
        cat2 = request.form['cat-2']
        cat3 = request.form['cat-3']
        con = sqlite3.connect('new_db.db')
        cur = con.cursor()
        cur.execute("UPDATE users SET IntCat1=?, IntCat2=?, IntCat3=? WHERE username=? and password=?", (cat1, cat2, cat3, username, password))
        con.commit()

        return redirect(url_for("views.main_page"))

    return render_template('choice.html')


@views.route("/main_page", methods=['GET', 'POST'])
def main_page():
    D = dict()
    username = session['username']
    password = session['password']
    con = sqlite3.connect('new_db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? and password=?", (username, password))
    user_data = cur.fetchone()
    user_country = user_data[6]
    news_lmt = user_data[7]
    user_cat1 = user_data[8]
    user_cat2 = user_data[9]
    user_cat3 = user_data[10]

    cur.execute("SELECT Title, Description, link FROM news_data WHERE Country=? and Category=?",
                (user_country, user_cat1))

    nw1 = cur.fetchall()
    nw1.reverse()

    cur.execute("SELECT Title, Description, link FROM news_data WHERE Country=? and Category=?",
                (user_country, user_cat2))

    nw2 = cur.fetchall()
    nw2.reverse()

    cur.execute("SELECT Title, Description, link FROM news_data WHERE Country=? and Category=?",
                (user_country, user_cat3))

    nw3 = cur.fetchall()
    nw3.reverse()

    if news_lmt == '':
        news_lmt = 10

    if news_lmt == 'N/A':
        news_lmt = 10
    
    nw_lmt = int(news_lmt)

    size_nw1 = len(nw1)
    if size_nw1 > nw_lmt:
        size_nw1 = nw_lmt
    size_nw2 = len(nw2)
    if size_nw2 > nw_lmt:
        size_nw2 = nw_lmt
    size_nw3 = len(nw3)
    if size_nw3 > nw_lmt:
        size_nw3 = nw_lmt

    cur.execute("SELECT username, location, IntCat1, IntCat2, IntCat3 FROM users WHERE username!=? and password!=?",
                (username, password))
    data = cur.fetchall()

    fsz = len(data)

    for x in range(fsz):
        frd_ind = 0
        for y in range(5):
            print(data[x][y])
            if user_country == data[x][y]:
                frd_ind += 1
            if user_cat1 == data[x][y]:
                frd_ind += 1
            if user_cat2 == data[x][y]:
                frd_ind += 1
            if user_cat3 == data[x][y]:
                frd_ind += 1
        print(frd_ind)
        frd_uname = data[x][0]
        D[frd_uname] = int(frd_ind)

    print(D)
    D_new = dict(sorted(D.items(), key=lambda item: item[1], reverse=True))
    print(D_new)

    return render_template('main_page.html', Title1=nw1, Sz1=size_nw1, Title2=nw2, Sz2=size_nw2, Title3=nw3, Sz3=size_nw3,
                           Cat1=user_cat1, Cat2=user_cat2, Cat3=user_cat3)


@views.route("/old_page", methods=['GET'])
def old_page():
    username = session['username']
    password = session['password']
    con = sqlite3.connect('new_db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? and password=?", (username, password))
    user_data = cur.fetchone()
    user_country = user_data[6]
    user_cat1 = user_data[8]
    user_cat2 = user_data[9]
    user_cat3 = user_data[10]

    nw_dt2 = nw_dt - datetime.timedelta(days=1)

    cur.execute("SELECT Title, Description, link FROM news_data WHERE Country=? and Category=? and Nw_Date=?",
                (user_country, user_cat1, nw_dt2))

    nw1 = cur.fetchall()

    cur.execute("SELECT Title, Description, link FROM news_data WHERE Country=? and Category=? and Nw_Date=?",
                (user_country, user_cat2, nw_dt2))

    nw2 = cur.fetchall()

    cur.execute("SELECT Title, Description, link FROM news_data WHERE Country=? and Category=? and Nw_Date=?",
                (user_country, user_cat3, nw_dt2))

    nw3 = cur.fetchall()

    size_nw1 = len(nw1)
    size_nw2 = len(nw2)
    size_nw3 = len(nw3)

    return render_template('old_page.html', Title1=nw1, Sz1=size_nw1, Title2=nw2, Sz2=size_nw2, Title3=nw3, Sz3=size_nw3, Cat1=user_cat1, Cat2=user_cat2, Cat3=user_cat3)


@views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == "POST":
        username = form.username.data
        password = form.password.data
        con = sqlite3.connect('new_db.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=? and password=?", (username, password))
        user_data = cur.fetchone()

        if user_data:
            if user_data[0] == username and user_data[5] == password:
                print("Successfully Logged In")
                session['username'] = username
                session['password'] = password
                session['email'] = user_data[4]
                return redirect(url_for("views.main_page"))
        else:
            print("Incorrect credentials")
            msg = 'Incorrect credentials'
            return render_template('login.html', form=form, message=msg)


    return render_template('login.html', form=form)


@views.route("/profile", methods=['GET', 'POST'])
def profile_update():
    username = session["username"]
    password = session["password"]
    email = session["email"]
    con = sqlite3.connect('new_db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? and password=?", (username, password))
    user_data = cur.fetchone()
    firstname = user_data[2]
    lastname = user_data[3]
    country = user_data[6]
    news_lmt = user_data[7]
    user_cat1 = user_data[8]
    user_cat2 = user_data[9]
    user_cat3 = user_data[10]

    if request.method == 'POST':
        cat1 = request.form['cat-1']
        cat2 = request.form['cat-2']
        cat3 = request.form['cat-3']
        news_lmt = request.form['newslmt']
        print(news_lmt)
        cur.execute("UPDATE users SET IntCat1=?, IntCat2=?, IntCat3=?, location2=? WHERE username=? and password=?",
                    (cat1, cat2, cat3, news_lmt, username, password))
        con.commit()
        msg = 'Profile successfully updated!!!'
        return render_template('profile_update.html', username=username, email=email, country=country, firstname=firstname,
                               lastname=lastname, cat1=cat1, cat2=cat2, cat3=cat3, news_lmt=news_lmt, message=msg)

    return render_template('profile_update.html', username=username, email=email, firstname=firstname, news_lmt=news_lmt,
                           lastname=lastname, country=country, cat1=user_cat1, cat2=user_cat2, cat3=user_cat3)

@views.route("/profile2", methods=['GET', 'POST'])
def profile_update2():
    username = session["username"]
    password = session["password"]
    email = session["email"]
    con = sqlite3.connect('new_db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? and password=?", (username, password))
    user_data = cur.fetchone()
    firstname = user_data[2]
    lastname = user_data[3]
    country = user_data[6]
    user_cat1 = user_data[8]
    user_cat2 = user_data[9]
    user_cat3 = user_data[10]

    if request.method == 'POST':
        nw_firstname = request.form['firstname']
        nw_lastname = request.form['lastname']
        nw_country = request.form['country']
        cur.execute("UPDATE users SET location=?, firstname=?, lastname=? WHERE username=? and password=?",
                    (nw_country, nw_firstname, nw_lastname, username, password))
        con.commit()
        msg = 'Profile successfully updated!!!'
        return render_template('profile_update.html', username=username, email=email, country=nw_country, firstname=nw_firstname,
                               lastname=nw_lastname, cat1=user_cat1, cat2=user_cat2, cat3=user_cat3, message=msg)

    return render_template('profile_update.html', username=username, email=email, firstname=firstname,
                            lastname=lastname, country=country, cat1=user_cat1, cat2=user_cat2, cat3=user_cat3)


@views.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("views.index"))
