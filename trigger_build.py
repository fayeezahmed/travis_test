#!/usr/bin/env

import os
import urllib
import requests
import subprocess

os.chdir('..')
subprocess.run(['ls', '-l'])

subprocess.run(['git', 'clone', 'https://github.com/fayeezahmed/postman_travis.git'])
os.chdir('postman_travis')
git_commit_hash = subprocess.run(['git', 'rev-parse', 'HEAD'])
post_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Travis-API-Version": "3",
    "Authorization": "token {}".format(os.environ['TRAVIS_ACCESS_TOKEN']),
}

post_body = {
"request": {
"message":"Trigger build at fayeezahmed/postman_travis commit: {}".format(git_commit_hash),
"branch":"master"
}}

url = 'https://api.travis-ci.org/repo/fayeezahmed%2Fpostman_travis/requests'

# req = urllib.request.Request(url, post_body, headers)
req = requests.post(url, headers=post_headers, data=post_body)
print(req)
