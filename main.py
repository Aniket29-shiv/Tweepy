import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("7wmvU0hecAY5A94ZRi5KckTgi", 
    "lBZj5PVS9vzlrJHyoAU8tf6oEA3OEzYaMLO1dUPxuzGjOpJY8S")
auth.set_access_token("776410329446088710-2GdPc3H9K2mkyaIxtDEzIshYokPeH37", 
    "iueq70n8EAuyzFLXjSOGsycBj9hg9dp3EwcKVCDc5fiNz")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

# Methods for User Timelines
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

#Methods for tweets
api.update_status("Test tweets from Tweepy Python!")

# Methods for Users
user = api.get_user("aniket2971")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

# Methods for followers
api.create_friendship("realpython")

# Methods for your account
api.update_profile(description="I like Python!")

# Methods for likes
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

# Methods for Searches
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

# Methods for Streaming
import json
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])