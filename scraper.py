import argparse
import re
import requests

resp = requests.get('https://xkcd.com/353/')
# print(help(resp))
print(resp.text)

# email regex:
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# url regex:
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

# phone regex:
# 1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description='Scrapes a single web page, extracting any URLs,
        'email addresses, and phone numbers it contains')
    parser.add_argument('url', help='Url to be scraped', nargs=1)
    return parser


def main():
    """Implementation of Scraper"""
    parser = create_parser()
