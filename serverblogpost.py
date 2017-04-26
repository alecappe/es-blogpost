#!/usr/bin/env python
import sqlite3
from flask import Flask, render_template, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('blog.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()

class PostBlog(Resource):
    def post(self):
        params = [
            request.form['title'],
            request.form['data'],
            request.form['post']
        ]
        sql = ''' insert into posts(title, data, post)
                values(?,?,?)'''

        c.execute(sql,params)
        conn.commit()
        return '', 201

@app.route('/', methods=['GET','POST'])
def index():
    sql = 'SELECT * FROM posts'
    ctx = {'posts': c.execute(sql)}

    return render_template('index.html', **ctx)

api.add_resource(PostBlog, '/posts')

if __name__ == '__main__':
    app.run(debug=True)
