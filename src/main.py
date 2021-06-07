from datetime import datetime
import base64
import requests
import facebook_scraper as scraper

from profileData import cur_credentials, target_profiles

target_profile = {'id': "123456789", 'name': "shirly.dwek"}
date_format_string = "%Y-%m-%dT%H:%M:%S"

target_posts = scraper.get_posts(
    target_profile['name'], credentials=cur_credentials, pages=1)
formatted_posts = [{'text': curPost['post_text'],
                    'publish_date': (curPost['time'].strftime(date_format_string)
                                     if curPost['time'] is not None
                                     else None),
                    'scraping_date': datetime.now().strftime(date_format_string)}
                   for curPost in target_posts]
print("done")
