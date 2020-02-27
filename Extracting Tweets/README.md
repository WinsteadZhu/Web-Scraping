# Extracting Tweets
The `twitter_query.py` program works with the `Tweepy` library for navigating the Twitter API to extract the Tweet (or status) contents of a specified user. It takes a Twitter user's handle as well as an optional `N` as arguments and returns the user's `N`-most recent Tweets, as well as the time of posting. If `N` is not specified, it returns only the single most recent Tweet.

## Credentials
When navigating the Twitter API, the required credentials can be retrieved  from the JSON file called `twitter_credentials.json`.

## Densign
This program defines two functions: `date_time_conversion` and `get_tweets`.

### `date_time_conversion`
The function `date_time_conversion` takes a string in the format `2020-02-26 14:22:26` and converts it into `2:22 PM, Feb 26, 2020`.

### `get_tweets`
The function `get_tweets` takes a Twitter user's handle as well as an optional `N` as arguments and returns a list of user's `N`-most recent Tweets, as well as the time of posting. The format of the posting time is converted by calling the function `date_time_conversion`.

### Twitter API
The program first retrieves the set of Twitter API credentials from a JSON file and creates an OAuthHandler instance. Then it <em>tries</em> to take one or two arguments and call the function `get_tweets`. Finally it <em>tries</em> to print the elements of the returned list of tweets, unless a `TweepError` is captured, in which case the message `*USER NOT FOUND*` will be shown.

## Usage
Call one or two arguments to the program script, where the first argument (a string) specifies the user's handler and the second optional argument (an integer) specifies the number of most recent tweets to be returned.

Two examples:

    % python3 twitter_query.py Huawei_Europe 3

where the output will be:

    3:57 PM, Feb 27, 2020:RT @HuaweiFr: #Huawei va installer en France une usine de production d'équipements radios pour la #5G, qui va créer 500 emplois directs. Le…
    3:56 PM, Feb 27, 2020:RT @PacdWeu: #Huawei will build its first European manufacturing plant in #France. The world leading #5G provider would invest 200 million…
    9:00 AM, Feb 27, 2020:RT @Huawei: At the #5GBringNewValue event in London, Huawei unveiled how its incredible new #5G products and solutions will bring more busi…

or input only one argument:

    % python3 twitter_query.py Huawei_Europe

which will produce the output as follows:

    3:57 PM, Feb 27, 2020:RT @HuaweiFr: #Huawei va installer en France une usine de production d'équipements radios pour la #5G, qui va créer 500 emplois directs. Le…







