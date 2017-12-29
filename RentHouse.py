from flask import Flask
from bd import db
import config
import flask
from models import Homes_inf
import mysql.connector
import json



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    page = flask.request.args.get('page',1,type=int)
    pagination = Homes_inf.query.paginate(page, per_page=10, error_out=False)
    messages = pagination.items
    return flask.render_template('index.html',messages=messages,pagination=pagination)

@app.route('/search',methods=['GET','POST'])
def search():
    page = flask.request.args.get('page', 1, type=int)
    text = flask.request.form['search']
    pagination = Homes_inf.query.filter(Homes_inf.info.like('%{}%'.format(text))).paginate(page, per_page=10, error_out=False)
    messages = pagination.items
    # context={
    #     'message': Homes_inf.query.filter(Homes_inf.info.like('%{}%'.format(text)))
    # }
    return flask.render_template('index.html',messages=messages,pagination=pagination )

@app.route('/data_analysis',methods=['GET','POST'])
def to_data():
    if flask.request.method=='POST':
        conn = mysql.connector.connect(user='root',password='12341234',database='homes')
        cursor = conn.cursor()
        cursor.execute('SELECT release_time,count(*) FROM homes_info GROUP BY release_time;')
        values = cursor.fetchall()
        data = {}
        for i in range(0, len(values)):
            data[str(values[i][0])] = int(values[i][1])
        json_data = json.dumps(data)
        cursor.close()
        conn.close()
        return json_data
    else:
        return flask.render_template('data.html')
@app.route('/data_analysis1',methods=['GET','POST'])
def to_data1():
    if flask.request.method=='POST':
        conn = mysql.connector.connect(user='root',password='12341234',database='homes')
        cursor = conn.cursor()
        cursor.execute('SELECT area,avg(price) FROM homes_info GROUP BY area')
        values = cursor.fetchall()
        cursor.close()
        conn.close()
        data = {}
        for i in range(0, len(values)):
            data[values[i][0]] = int(values[i][1])
        json_data = json.dumps(data)
        return json_data
    else:
        return flask.render_template('data1.html')

@app.route('/pudong',methods=['GET','POST'])
def pudong():
    if flask.request.method == 'POST':
        area = flask.request.form.get('area')
        print(area)
        conn = mysql.connector.connect(user='root', password='12341234', database='homes')
        cursor = conn.cursor()
        cursor.execute("SELECT house_type, AVG(price) from homes_info WHERE area=%s GROUP BY house_type"%(area) )
        values = cursor.fetchall()
        cursor.close()
        conn.close()

        data = {}
        for i in range(0, len(values)):
            data[values[i][0]] = int(values[i][1])
        json_data = json.dumps(data)
        return json_data
    else:
        area = flask.request.args.get('area')
        print(area)
        return flask.render_template('pudong.html')

if __name__ == '__main__':
    app.run()


