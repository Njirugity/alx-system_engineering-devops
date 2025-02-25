#!/usr/bin/python3
""" function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a
given subreddit"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and rints the titles of the
    first 10 hot posts listed for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux: 0x16.api.advanced: v1.0.0 (by /u/briyothedon)"
        }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 400:
        return ("None")
    data = response.json().get("data")
    if not data:
        print("None")
    else:
        titles = []
        for i in data.get("children"):
            title = i.get("data").get("title")
            titles.append(title)
        print(titles)
