import TwitterSearch

# This file is the feeder getting text from a Twitter user tweets.

def get_user_tweet(twitter_user):
    """ The argument twitter_user should be the twitter handle of the user you want to access the tweets of (without the
    @)."""
    try:
        tuo = TwitterSearch.TwitterUserOrder(twitter_user)
        ts = TwitterSearch(
            consumer_key = 'aaabbb',
            consumer_secret = 'cccddd',
            access_token = '111222',
            access_token_secret = '333444'
        )

        # start asking Twitter about the timeline
        for tweet in ts.search_tweets_iterable(tuo):
            yield tweet['text']

    except TwitterSearch.TwitterSearchException as e:
        print(e)

if __name__ == '__main__':
    get_user_tweet(616161516161321351351533)