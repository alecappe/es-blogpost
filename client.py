#!/usr/bin/env python
import requests
import argparse
import datetime


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--title', dest='title')
	parser.add_argument('--article', dest='article')
	args = parser.parse_args()

	title = args.title
	date = datetime.datetime.today()
	date = '{}-{}-{}'.format(date.day, date.month, date.year)
	article = args.article
	
	data = {
		'title': title,
		'data': date,
		'post': article
	}
	
	r = requests.post('http://127.0.0.1:5000/posts', data)
