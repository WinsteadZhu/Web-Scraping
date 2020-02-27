import tweepy
from tweepy.error import TweepError
import json
import csv
import sys


# Define a function that takes a date-time string and converts it into a time-date string,
# e.g. convert '2020-02-26 14:22:26' into '2:22 PM, Feb 26, 2020'
def date_time_conversion(date_time):

    # Retrieve date and time
    date, time = date_time.split()
    
    # Retrieve year, month and day from date
    year, month, day = date.split('-')
    
    # Convert month from number to abbreviation
    if month == '01':
        month_new = 'Jan'
    elif month == '02':
        month_new = 'Feb'
    elif month == '03':
        month_new = 'Mar'
    elif month == '04':
        month_new = 'Apr'
    elif month == '05':
        month_new = 'May'
    elif month == '06':
        month_new = 'June'
    elif month == '07':
        month_new = 'July'
    elif month == '08':
        month_new = 'Aug'
    elif month == '09':
        month_new = 'Sept'
    elif month == '10':
        month_new = 'Oct'
    elif month == '11':
        month_new = 'Nov'
    elif month == '12':
        month_new = 'Dec'
    
    # Retrieve hour, minute and second from time
    hour, minute, second = time.split(':')
    
    # Convert hour convention from 24-hour clock to 12-hour clock
    hour = int(hour)
    if hour > 12:
        meridies = 'PM'
        if hour != 12:
            hour_new = hour - 12
    else:
        hour_new = hour
        meridies = 'AM'
    hour_new = str(hour_new)
    
    time_date = hour_new + ':' + minute + ' ' + meridies + ', ' + month_new + ' ' + day + ', ' + year
    return time_date


# Define a function that takes a Twitter user’s handle and an optional integer as arguments
def get_tweets(handle, N=1):

    # Get the user object for twitter
    user = api.get_user(handle)
    
    # Return the N (=num) most recent statuses posted from the user specified
    tweets = api.user_timeline(screen_name=handle, count=N)
    
    # Convert time convention
    Tweets = []
    for tweet in tweets:
        tweet = date_time_conversion(str(tweet.created_at)) + ':' + tweet.text
        Tweets.append(tweet)
    
    return Tweets


# Load Twitter API credentials
with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_token = info['ACCESS_TOKEN']
    access_token_secret = info['ACCESS_TOKEN_SECRET']

# Create an OAuthHandler instance from the stored access token
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Enable calling argument(s) with the second argument as optional
first_arg = sys.argv[1]
try:
    second_arg = int(sys.argv[2])
except IndexError:
    second_arg = 1

# Get the user's Twitter content unless the user is not found
try:
    Tweets = get_tweets(first_arg, N=second_arg)
    for tweet in Tweets:
        print(tweet)
except TweepError:
    print('*USER NOT FOUND*')

