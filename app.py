from flask import Flask
from flask_bootstrap import Bootstrap
from views import views
from auths import auths
from models import news_fetch1, news_fetch2
from keys import key1, key2, key3, key4, key5, key6, key7, key8, key9, key10, key11, key12, key13, key14, key15, key16, key17, key18, key19, key20, key21, key22, key23
from flask_apscheduler import APScheduler
import datetime
import sqlite3


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ProjectBlueBook'
app.config.from_object(Config())
app.config['SQLACHEMY_DATABASE_URI'] = 'postgres://adffdgsrywxhsa:d483d23a6d3ac240757343c3b1ab826b05e8211a219306a9b271da8b964ee6f7@ec2-54-174-31-7.compute-1.amazonaws.com:5432/ddi35hde1c4juj'

Bootstrap(app)
scheduler = APScheduler()
scheduler.init_app(app)

con = sqlite3.connect('new_db.db')
cur = con.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS users (username TEXT, 
                                        fullname TEXT,
                                        firstname TEXT,
                                        lastname TEXT, 
                                        email TEXT, 
                                        password TEXT, 
                                        location TEXT,
                                        location2 TEXT, 
                                        IntCat1 TEXT, 
                                        IntCat2 TEXT, 
                                        IntCat3 TEXT)
    """)


app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auths, url_prefix='/')


@scheduler.task('cron', id='1', hour='02', minute='58')
def news_fetch():
    news_fetch1('business', 'australia', key23)
    news_fetch1('sports', 'australia', key23)
    news_fetch1('health', 'australia', key23)
    news_fetch1('health', 'canada', key23)
    news_fetch1('technology', 'canada', key13)


scheduler.start()

if __name__ == '__main__':
    app.run()