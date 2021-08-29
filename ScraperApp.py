import os, requests, pandas
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

@app.route('/submitTwitterHandle', methods = ['POST'])
def run_twitter_scraper():
	twitterHandle = request.form['twitterHandle']
	print("Desired handle: " + twitterHandle)
	try:
		os.system('twint -u ' + twitterHandle + ' -o json/' + twitterHandle + '_scrape.json --json --timeline')

		# We now have the scrape data in JSON format, but we also want it in CSV. Although twint offers CSV, it's messy and incomplete. Instead of using twint
		# to generate the CSV output, therefore, we should route convert the json data to a pandas dataframe and save it as CSV.
		df = pandas.read_json('json/' + twitterHandle + '_scrape.json', lines = True)
		df.to_csv('csv/' + twitterHandle + '_scrape.csv')

		if request.form['downloadCSV']:
			return send_from_directory('csv', twitterHandle + '_scrape.csv')
		elif request.form['downloadJSON']:
			return send_from_directory('json', twitterHandle + '_scrape.json')
		else:
			return "Successfully ran scrape"
	except:
		return "Scrape failed."

@app.route('/instagramScraper')
def instagramHome():
	return render_template('instagram_home.html')

@app.route('/facebookScraper')
def facebookHome():
	return render_template('facebook_home.html')

