import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("7wmvU0hecAY5A94ZRi5KckTgi")
    consumer_secret = os.getenv("lBZj5PVS9vzlrJHyoAU8tf6oEA3OEzYaMLO1dUPxuzGjOpJY8S")
    access_token = os.getenv("776410329446088710-2GdPc3H9K2mkyaIxtDEzIshYokPeH37")
    access_token_secret = os.getenv("iueq70n8EAuyzFLXjSOGsycBj9hg9dp3EwcKVCDc5fiNz")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api