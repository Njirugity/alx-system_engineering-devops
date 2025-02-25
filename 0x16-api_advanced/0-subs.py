#!/usr/bin/python3
"""Function to query a subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux: 0x16.api.advanced: v1.0.0 (by /u/briyothedon)"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 400:
        return 0
    data = response.json().get("data")
    if not data:
        return 0
    return data.get("subscribers")
