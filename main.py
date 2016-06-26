import io
import json
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

params = {
    'term': 'chinese food',
    'lang': 'ch',
}

result = client.search('monterey', **params)

print 'name, distance, score, address'

for business in result.businesses:
	print '{0}, {1}, {2} out of 5, {3}'.format(business.name, business.distance, business.rating, business.location.display_address)


