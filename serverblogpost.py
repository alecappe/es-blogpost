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
    
if __name__ == '__main__':
    app.run(debug=True)
