import os
from flask import Flask
from flask import render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def homePage():
	os.system('pwd ; ls ; ls images')
	return render_template('home.html')

@app.route('/redditScraper')
def redditHome():
	return render_template('reddit_home.html')

@app.route('/twitterScraper')
def twitterHome():
	return render_template('twitter_home.html')

@app.route('/instagramScraper')
def instagramHome():
	return render_template('instagram_home.html')

@app.route('/facebookScraper')
def facebookHome():
	return render_template('facebook_home.html')
