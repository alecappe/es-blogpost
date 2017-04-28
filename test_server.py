#!/usr/bin/env python
from peewee import *
from serverblogpost import app
from serverblogpost import Posts
from http.client import CREATED
from http.client import OK
from http.client import BAD_REQUEST
import json

    
class TestBlog:
	@classmethod
	def setup_class(cls):
		Posts._meta.database = SqliteDatabase(':memory:')
		Posts.create_table()
		cls.app = app.test_client()

	def setup_method(self):
		Posts.delete().execute()

	def test_get_db_empty(self):
		resp = self.app.get('/posts')
		assert resp.status_code == OK
		assert json.loads(resp.data.decode()) == []

	def test_get_db(self):
		Posts.create(title='TitleTest', post='PostTest')
		Posts.create(title='TitleTest2', post='PostTest2')

		select_post = Posts.select()
		dbposts_list = []
		for post in select_post:
			dbposts_list.append({'title': post.title, 'post': post.post})

		resp = self.app.get('/posts')

		assert resp.status_code == OK
		assert json.loads(resp.data.decode()) == dbposts_list

	def test_post_success(self):
		data = { 'title': 'Simple title', 'post': 'Simple Post'}
		resp = self.app.post('/posts', data=data)

		select_post = Posts.select()
		dbposts_list = []
		for post in select_post:
			dbposts_list.append({'title': post.title, 'post': post.post})

		assert len(select_post) == 1
		assert resp.status_code == CREATED
		assert json.loads(resp.data.decode()) == dbposts_list

	def test_post_empty_field(self):
		data = { 'title': '', 'post': 'Simple Post'}
		resp = self.app.post('/posts', data=data)

		select_post = Posts.select()
		dbposts_list = []
		for post in select_post:
			dbposts_list.append({'title': post.title, 'post': post.post})

		assert resp.status_code == BAD_REQUEST

	def test_post_missing_posttext(self):
		data = { 'title': 'Simple title'}
		resp = self.app.post('/posts', data=data)

		select_post = Posts.select()
		posts_list = []
		for post in select_post:
			posts_list.append({'title': post.title, 'post': post.post})

		assert resp.status_code == BAD_REQUEST

	def test_post_missing_titlepost(self):
		data = { 'post': 'Simple post'}
		resp = self.app.post('/posts', data=data)

		select_post = Posts.select()
		posts_list = []
		for post in select_post:
			posts_list.append({'title': post.title, 'post': post.post})

		assert resp.status_code == BAD_REQUEST

