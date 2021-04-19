import os
import json
import requests
import tweepy

def get_random_dog(filename: str='temp') -> None:
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    rd = json.loads(r.content)
    r2 = requests.get(rd['message'])

    with open(filename, 'wb') as image:
        for chunk in r2:
            image.write(chunk)

def main(message: str, filename: str='temp') -> None:
    auth = tweepy.OAuthHandler(
        os.environ.get('TWITTER_API_KEY'),
        os.environ.get('TWITTER_API_SECRET')
    )
    auth.set_access_token(
        os.environ.get('TWITTER_ACCESS_TOKEN'),
        os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)
    get_random_dog(filename)

    try:
        api.verify_credentials()
        print("Twitter Authentication Succeeded")

        try:
            api.update_with_media(filename, status=message)
            print('Tweet successfully sent!')

        except Exception as e:
            print('Error sending tweet \n %s' % e)
    except:
        print("Twitter AUthentication Failed")


if __name__ == '__main__':
    m0 = "Hey, @camdotbio! 👋 \n\nHere's your daily dog photo!"
    m1 = "\n\nLearn how to automate dog photos here: https://bit.ly/3cVTQN3"
    main(message=m0 + m1)
