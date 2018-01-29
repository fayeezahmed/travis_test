#!/usr/bin/env

import os
import urllib
import requests
import subprocess


def trigger_build(git_url=""):
    """
    This function triggers a build on travis on the specified git repository. To be used within other repositories' travis scripts.

    @param git_url: this is the git url, in the format repo_account/repo_name
    """

    try:
        if not git_url:
            raise ValueError("Please specify a git url in the following format https://github.com/repo_account/repo_name.git")
    except ValueError as e:
        print(e)

    os.chdir("..")
    subprocess.run(["git", "clone", "https://github.com/{0}.git".format(git_url)])

    git_url_split = git_url.split("/")
    group_repo_name = git_url_split[0]
    repo_name = git_url_split[1]

    os.chdir(repo_name)

    git_commit_hash = subprocess.run(["git", "rev-parse", "HEAD"])

    post_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Travis-API-Version": "3",
        "Authorization": "token {}".format(os.environ["TRAVIS_ACCESS_TOKEN"]),
    }

    post_body = '{{"request": {{"message":"Trigger build at fayeezahmed/postman_travis commit: {0}}}","branch":"master"}}}}'.format(git_commit_hash)

    url = "https://api.travis-ci.org/repo/{0}%2F{1}/requests".format(group_repo_name, repo_name)

    req = requests.post(url, headers=post_headers, data=post_body)

trigger_build("fayeezahmed/postman_travis")
