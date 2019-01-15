from unsplash.api import Api
from unsplash.auth import Auth
import urllib.request
import os
from appscript import app, mactypes

client_id = "77c38f1c232cbdde899e5163dce6572efa82d4275f6eb4614e5bf3a6a05c0843"
client_secret = "3297d26247dfeb2ff322ddeef19b93c7ee0e3c55712a687915da7227ef1dab7d"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)
photo = api.photo.random(featured=True, orientation="landscape")
url = photo[0].links.download
urllib.request.urlretrieve(url, os.getcwd() + '/newimage.jpg')
app('Finder').desktop_picture.set(mactypes.File(os.getcwd() + '/newimage.jpg'))
