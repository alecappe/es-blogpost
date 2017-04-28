#!/usr/bin/env python
from peewee import *
from flask import Flask
from flask import render_template
from flask import request
from http.client import CREATED
from http.client import NO_CONTENT
from http.client import NOT_FOUND
from http.client import OK
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse


app = Flask(__name__)
api = Api(app)

db = SqliteDatabase('blog2.db')
db.connect()

class Posts(Model):
    title = TextField()
    data = DateTimeField(default=[SQL('CURRENT_TIMESTAMP')])
    post = TextField()

    class Meta:
        database = db

def non_empty_str(val, name):
    if not str(val).strip():
        raise ValueError('The argument {} is not empty'.format(name))
    return str(val)

class Blogpost(Resource):
    def get(self):
        post_list = []
        db_blog = Posts.select()
        for post in db_blog:
            post_list.append({'title': post.title, 'post': post.post})
        return post_list, OK

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=non_empty_str, required=True)
        parser.add_argument('post', type=non_empty_str, required=True)
        args = parser.parse_args(strict=True)

        Posts.create(title=args['title'], post=args['post'])

        return '', CREATED

@app.route('/')
def get():
    resp_get = Posts.select()
    ctx = {'posts': resp_get}

    return render_template('index.html', **ctx)

api.add_resource(Blogpost, '/posts')

if __name__ == '__main__':
    Posts.create_table(fail_silently=True)
    app.run(debug=True)
