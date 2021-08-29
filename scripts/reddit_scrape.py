#!/usr/bin/python3
'''
Seth R King
A script used to scrape Reddit for post data given a number of desired posts, subreddit name, listing order, and timeframe. 
The script dumps the JSON results to a subfolder on the server to be returned to the user or parsed to an HTML template.
27 August 2021
'''
import requests


def main():
	input = input("Enter the Reddit scrape information (subreddit name, limit count, listing order, and timeframe, in that order):")
	input = input.split(" ") # This will eventually be collected via an HTML form and piped into the script execution
	subreddit = input[0]
	limit = input[1]
	listingOrder = input[2]
	timeframe = input[3]

	url = "https://www.reddit.com/r/" + subreddit + '/' + listingOrder + '.json?limit=' + limit + '&t=' + timeframe
	print("Generated URL: " + url)
	result = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
	#print(str(data.text))

	# Write the json data to an outfile
	with open("json/" + subreddit + '_scrape.json', 'w') as outfile:
		outfile.write(data.text)
		outfile.close()

	result = result.json()
	parseResults(result)

# Parse the resulting JSON to an HTML page
def parseResults(result):
	outfile = open('templates/' + subreddit + '_scrape.html', 'w')

	for child in result['data']['children']:
		postText = child['data']['selftext']
		user = child['data']['author']
		title = child['data']['title']


