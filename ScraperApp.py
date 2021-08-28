import os, requests
from flask import Flask
from flask import render_template, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def homePage():
	os.system('pwd ; ls ; ls images')
	return render_template('home.html')

@app.route('/home')
def routeHome():
	return render_template('home.html')

@app.route('/redditScraper')
def redditHome():
	return render_template('reddit_home.html')

@app.route('/submitRedditHandle', methods=['POST'])
def run_reddit_scraper():
	subredditID = request.form['subredditID']
	limit = request.form['limit']
	listingOrder = request.form['listingOrder']
	timeframe = request.form['timeframe']

	print("Subreddit ID: " + subredditID + " Limit: " + limit)
	inputstring = subredditID + " " + limit + " " + listingOrder + " " + timeframe

	# Run the Scraper script with the given input (should implement input validation later)
	try:
		os.system("echo '" + inputstring + "' | ./scripts/reddit_scrape.py")
	except:
		print("Experienced an error with the script execution.")

	return send_from_directory('json', subredditID + "_scrape.json") # Eventually will give options of returning JSON, CSV, or parsed HTML

@app.route('/twitterScraper')
def twitterHome():
	return render_template('twitter_home.html')

@app.route('/instagramScraper')
def instagramHome():
	return render_template('instagram_home.html')

@app.route('/facebookScraper')
def facebookHome():
	return render_template('facebook_home.html')

