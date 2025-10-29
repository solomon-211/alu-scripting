#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
If it is an invalid subreddit, the function returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "CustomUserAgent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except Exception:
        return 0
