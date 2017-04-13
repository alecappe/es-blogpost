#!/usr/bin/env python
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
conn = sqlite3.connect('blog.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        sql = 'SELECT * FROM posts'
        ctx = {'posts': c.execute(sql)}
        return render_template('index.html', **ctx)

    elif request.method == 'POST':
        params = [
            request.form['title'],
            request.form['data'],
            request.form['post']
        ]
        sql = ''' insert into posts(title, data, post)
                values(?,?,?)'''
        c.execute(sql,params)
        conn.commit()
        return '',201

if __name__ == '__main__':
    app.run(debug=True)
