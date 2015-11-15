

# Client id
# J0VYNNTNRYQR5HLYN315N1ELJNU2CK0P0OCUHVGSL2RWGH2P
# Client secret
# 0WUZVVXTJMGJRIGFMIPWKLGJJLV1KGRKEZSC1RUZGYWOWH3F
#http://www.ajinkyamandhare.blogspot.com/?code=NGLMWZ1KO2J3IZ23TD3QQCQOUPJIVF4RAQFDPG30EWLVPIKI#_=_
#Access token:NKAE2UBIMNTW2BLXKFXOFO50ZXPSTWYQHEXMCSWCLKSX0PCW
import foursquare as f
import pyfoursquare as foursquare

# client_id = "J0VYNNTNRYQR5HLYN315N1ELJNU2CK0P0OCUHVGSL2RWGH2P"
# client_secret = "0WUZVVXTJMGJRIGFMIPWKLGJJLV1KGRKEZSC1RUZGYWOWH3F"
# callback = 'http://www.ajinkyamandhare.blogspot.com'
# 
# auth = foursquare.OAuthHandler(client_id, client_secret, callback)
# 
# auth_url = auth.get_authorization_url()
# print 'Please authorize: ' + auth_url
# 
# code = 'SREDMKG4FCVLIZL3DXTJFOOZ4T10SQ23GBHTGZV5E50IKWFK'

# access_token = auth.get_access_token(code)
# print 'Your access token is ' + access_token
# 
# api = foursquare.API(auth)
# 
# result = api.venues_search(query='Burburinho', ll='-8.063542,-34.872891')
# 
# print dir(result[0])
# 
# print result[0].name

client = f.Foursquare(access_token='NKAE2UBIMNTW2BLXKFXOFO50ZXPSTWYQHEXMCSWCLKSX0PCW')

print client.venues.explore(params={'ll':'40.7,-74'})

# print client.venues.tips(params={'ll':'40.7,-74'})