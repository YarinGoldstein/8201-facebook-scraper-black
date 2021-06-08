from datetime import datetime
import base64
import requests
import facebook_scraper as scraper

from profileData import cur_credentials, target_profiles

target_profile = [{'id': "123456789", 'name': "shirly.dwek"}, {
    'id': "123456799", 'name': "shirly.dwek"}]
date_format_string = "%Y-%m-%dT%H:%M:%S"

target_post_groups = [[cur_post for cur_post in scraper.get_posts(cur_profile['name'],
                                                                  credentials=cur_credentials,
                                                                  pages=1)]
                      for cur_profile
                      in target_profile]

formatted_post_groups = [cur_post_group[0]['post_text']
                         for cur_post_group in target_post_groups]

# formatted_posts = [{'text': curPost['post_text'],
#                     'publish_date': (curPost['time'].strftime(date_format_string)
#                                      if curPost['time'] is not None
#                                      else None),
#                     'scraping_date': datetime.now().strftime(date_format_string)}
#                    for curPost
#                    in target_posts]
print("done")
