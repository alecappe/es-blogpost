#!/usr/bin/env python
import requests
import argparse


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--title', dest='title', required=True)
	parser.add_argument('--article', dest='article', required=True)
	args = parser.parse_args()

	title = args.title
	
	article = args.article
	
	data = {
		'title': title,
		'post': article
	}
	
	r = requests.post('http://127.0.0.1:5000/posts', data=data)
