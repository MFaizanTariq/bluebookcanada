from flask import Flask
from flask_bootstrap import Bootstrap
from views import views
from auths import auths
from models import news_fetch1, news_fetch2
from keys import key1, key2, key3, key4, key5, key6, key7, key8, key9, key10, key11, key12, key13, key14, key15, key16, key17, key18
from flask_apscheduler import APScheduler
import datetime
import sqlite3


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ProjectBlueBook'
app.config.from_object(Config())

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


@scheduler.task('cron', id='1', hour='16', minute='11')
def news_fetch_cd1():
    news_fetch1('entertainment', 'australia', key10)


@scheduler.task('cron', id='2', hour='16', minute='12')
def news_fetch_cd2():
    news_fetch1('business', 'australia', key10)


@scheduler.task('cron', id='3', hour='16', minute='13')
def news_fetch_cd3():
    news_fetch1('sports', 'australia', key10)


@scheduler.task('cron', id='4', hour='16', minute='14')
def news_fetch_cd4():
    news_fetch1('health', 'australia', key10)


@scheduler.task('cron', id='5', hour='16', minute='15')
def news_fetch_cd5():
    news_fetch1('technology', 'australia', key10)


@scheduler.task('cron', id='6', hour='16', minute='16')
def news_fetch_cd6():
    news_fetch1('science', 'australia', key11)


@scheduler.task('cron', id='7', hour='16', minute='17')
def news_fetch_cd7():
    news_fetch1('entertainment', 'canada', key11)


@scheduler.task('cron', id='8', hour='16', minute='18')
def news_fetch_cd8():
    news_fetch1('business', 'canada', key11)


@scheduler.task('cron', id='9', hour='16', minute='19')
def news_fetch_cd9():
    news_fetch1('sports', 'canada', key11)


@scheduler.task('cron', id='10', hour='16', minute='20')
def news_fetch_cd10():
    news_fetch1('health', 'canada', key11)


@scheduler.task('cron', id='11', hour='16', minute='21')
def news_fetch_cd11():
    news_fetch1('technology', 'canada', key12)


@scheduler.task('cron', id='12', hour='16', minute='22')
def news_fetch_cd12():
    news_fetch1('science', 'canada', key12)


@scheduler.task('cron', id='13', hour='16', minute='23')
def news_fetch_cd13():
    news_fetch1('entertainment', 'india', key12)


@scheduler.task('cron', id='14', hour='16', minute='24')
def news_fetch_cd14():
    news_fetch1('business', 'india', key12)


@scheduler.task('cron', id='15', hour='16', minute='25')
def news_fetch_cd15():
    news_fetch1('sports', 'india', key12)


@scheduler.task('cron', id='16', hour='16', minute='30')
def news_fetch_cd16():
    news_fetch1('health', 'india', key18)


@scheduler.task('cron', id='17', hour='16', minute='31')
def news_fetch_cd17():
    news_fetch1('technology', 'india', key18)


@scheduler.task('cron', id='18', hour='16', minute='32')
def news_fetch_cd18():
    news_fetch1('science', 'india', key18)


@scheduler.task('cron', id='19', hour='16', minute='33')
def news_fetch_cd19():
    news_fetch1('entertainment', 'italy', key18)


@scheduler.task('cron', id='20', hour='16', minute='34')
def news_fetch_cd20():
    news_fetch1('business', 'italy', key18)


@scheduler.task('cron', id='21', hour='16', minute='35')
def news_fetch_cd21():
    news_fetch1('sports', 'italy', key14)


@scheduler.task('cron', id='22', hour='16', minute='36')
def news_fetch_cd22():
    news_fetch1('health', 'italy', key14)


@scheduler.task('cron', id='23', hour='16', minute='37')
def news_fetch_cd23():
    news_fetch1('technology', 'italy', key14)


@scheduler.task('cron', id='24', hour='16', minute='38')
def news_fetch_cd24():
    news_fetch1('science', 'italy', key14)


@scheduler.task('cron', id='25', hour='16', minute='39')
def news_fetch_cd25():
    news_fetch1('entertainment', 'united_kingdom', key14)


@scheduler.task('cron', id='26', hour='16', minute='40')
def news_fetch_cd26():
    news_fetch1('business', 'united_kingdom', key15)


@scheduler.task('cron', id='27', hour='16', minute='41')
def news_fetch_cd27():
    news_fetch1('sports', 'united_kingdom', key15)


@scheduler.task('cron', id='28', hour='16', minute='42')
def news_fetch_cd28():
    news_fetch1('health', 'united_kingdom', key15)


@scheduler.task('cron', id='29', hour='16', minute='43')
def news_fetch_cd29():
    news_fetch1('technology', 'united_kingdom', key15)


@scheduler.task('cron', id='30', hour='16', minute='44')
def news_fetch_cd30():
    news_fetch1('science', 'united_kingdom', key15)


@scheduler.task('cron', id='31', hour='16', minute='45')
def news_fetch_cd31():
    news_fetch1('entertainment', 'united_states', key16)


@scheduler.task('cron', id='32', hour='16', minute='46')
def news_fetch_cd32():
    news_fetch1('business', 'united_states', key16)


@scheduler.task('cron', id='33', hour='16', minute='47')
def news_fetch_cd33():
    news_fetch1('sports', 'united_states', key16)


@scheduler.task('cron', id='34', hour='16', minute='48')
def news_fetch_cd34():
    news_fetch1('health', 'united_states', key16)


@scheduler.task('cron', id='35', hour='16', minute='49')
def news_fetch_cd35():
    news_fetch1('technology', 'united_states', key16)


@scheduler.task('cron', id='36', hour='16', minute='50')
def news_fetch_cd36():
    news_fetch1('science', 'united_states', key17)


@scheduler.task('cron', id='37', hour='16', minute='51')
def news_fetch_cd37():
    news_fetch1('entertainment', 'germany', key17)


@scheduler.task('cron', id='38', hour='16', minute='52')
def news_fetch_cd38():
    news_fetch1('business', 'germany', key17)


@scheduler.task('cron', id='39', hour='16', minute='53')
def news_fetch_cd39():
    news_fetch1('sports', 'germany', key17)


@scheduler.task('cron', id='40', hour='16', minute='54')
def news_fetch_cd40():
    news_fetch1('health', 'germany', key17)


@scheduler.task('cron', id='41', hour='16', minute='56')
def news_fetch_cd41():
    news_fetch1('technology', 'germany', key7)


@scheduler.task('cron', id='42', hour='16', minute='57')
def news_fetch_cd42():
    news_fetch1('science', 'germany', key9)


scheduler.start()


if __name__ == '__main__':
    app.run(debug=True)

