import os
import json
import requests
import tweepy

def main(filename='temp'):
    message = "Hey @camdotbio 👋! Here's your daily dog photo!"
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(
        os.environ.get('TWITTER_API_KEY'), 
        os.environ.get('TWITTER_API_SECRET')
    )
    auth.set_access_token(
        os.environ.get('TWITTER_ACCESS_TOKEN'), 
        os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)
    
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    rs = json.loads(r.content)
    r2 = requests.get(rs['message'])
    with open(filename, 'wb') as image:
        for chunk in r2:
            image.write(chunk)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    try:
        #api.update_status(status='Updating using OAuth authentication via Tweepy!')
        api.update_with_media(filename, status=message)
    except Exception as e:
        print('Error during sending of tweet \n %s' % e)

if __name__ == '__main__':
    main()
