import base64
import hashlib
import os
import re

import requests
from requests_oauthlib import OAuth2Session

from config import oauth2_client_id, oauth2_client_secret, redirect_uri

client_id = oauth2_client_id
client_secret = oauth2_client_secret
auth_url = "https://twitter.com/i/oauth2/authorize"
token_url = "https://api.twitter.com/2/oauth2/token"
redirect_uri = redirect_uri

scopes = ['tweet.read', 'tweet.write', 'tweet.moderate.write', 'users.read', 'follows.read', 'follows.write',
          'offline.access', 'space.read', 'mute.read', 'mute.write', 'like.read', 'like.write', 'list.read',
          'list.write', 'block.read', 'block.write', 'bookmark.read', 'bookmark.write']

# Create a code verifier
code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

# Create a code challenge
code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
code_challenge = code_challenge.replace("=", "")


def make_token():
    return OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scopes)


def verify():
    twitter = make_token()
    authorization_url, state = twitter.authorization_url(
        url=auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    )
    print(authorization_url)
    print(state)

    # Handle the callback and complete the authorization process
    callback_url = input("Enter the callback URL after granting permission: ")
    token = twitter.fetch_token(
        token_url,
        authorization_response=callback_url,
        code_verifier=code_verifier,
        include_client_id=True,
        client_secret=client_secret,
    )

    print(twitter.authorized)
    print(code_verifier)

    return twitter, token


def post_tweets():
    twitter, token = verify()
    header = {"Authorization": f"Bearer {token['access_token']}",
              "Content-Type": "application/json"}
    # params = {
    #     "ids": "1627329264314990595",
    #     "tweet.fields": "public_metrics",
    #     'expansions': 'attachments.media_keys',
    #     'media.fields': 'public_metrics'
    # }
    url = 'https://api.twitter.com/2/tweets'
    json = {
        "text": "Are you feeling good today?",
        'poll': {
            'options': ['Yes', 'Maybe', 'No'],
            'duration_minutes': 1440
        }
    }
    response = twitter.post(url, headers=header, json=json)
    print(response.json())

post_tweets()
