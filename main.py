from unsplash.api import Api
from unsplash.auth import Auth
import urllib.request
import os
from appscript import app, mactypes
import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler


client_id = {} #check API for own ids
client_secret = {}
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = ""
auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)

sched = BlockingScheduler()

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=10) #This changes your background every weekday at 10AM as long as script is running
@sched.scheduled_job('interval', seconds=10) #Changes your background every 10 seconds 
def timed_job():
    photo = api.photo.random(featured=True, orientation="landscape")
    url = photo[0].links.download
    urllib.request.urlretrieve(url, os.getcwd() + '/newimage' + str(datetime.datetime.date(datetime.datetime.now())) + '.jpg')
    app('Finder').desktop_picture.set(mactypes.File(os.getcwd() + '/newimage' + str(datetime.datetime.date(datetime.datetime.now())) + '.jpg'))

sched.start()

