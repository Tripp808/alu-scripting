#!/usr/bin/python3

"""
This script queries the Reddit API and returns the number of subscribers for a given subreddit.
If the subreddit is invalid or any error occurs, it returns an appropriate error message.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int or str: The number of subscribers if the subreddit is valid, or an error message if invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent header

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if 'error' in data:
            if data['error'] == 404:
                return f"Subreddit '{subreddit}' does not exist."
            else:
                return "An error occurred while fetching subreddit data."
        subscribers = data['data']['subscribers']
        return subscribers
    except (requests.exceptions.RequestException, KeyError):
        return "An error occurred while fetching subreddit data."


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
