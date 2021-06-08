from datetime import datetime
import facebook_scraper as scraper
import json
import requests

from profileData import target_profiles
from imageService import get_image_from_post_group

date_format_string = "%Y-%m-%dT%H:%M:%S"
data_file_name = "data/postData.json"
request_ip = "http://intelligence-api-git-2-intelapp1.apps.openforce.openforce.biz/api/posts/addScraping"

target_post_groups = [[dict(cur_post, **{'person_id': cur_profile['person_id']})
                       for cur_post
                       in scraper.get_posts(cur_profile['user_id'],
                                            credentials=(
                                                cur_profile['email'], cur_profile['password']),
                                            pages=1)]
                      for cur_profile
                      in target_profiles]

formatted_post_groups = [{'person_id': cur_post_group[0]['person_id'],
                          'image': get_image_from_post_group(cur_post_group),
                          'name': cur_post_group[0]['username'],
                          'data': [{'text': curPost['post_text'],
                                    'publish_date': (curPost['time'].strftime(date_format_string)
                                                     if curPost['time'] is not None
                                                     else None),
                                    'scraping_date': datetime.now().strftime(date_format_string)}
                                   for curPost
                                   in cur_post_group]
                          }
                         for cur_post_group
                         in target_post_groups
                         if len(cur_post_group) > 0]
print("Info: Post scraping successful, saving data...")

data_file = open(data_file_name, 'w')
json.dump(formatted_post_groups, data_file)
data_file.close()
print("Info: Data saved at filepath '~/{}', creating a post request...".format(data_file_name))

response = requests.post(request_ip, json=json.dumps(formatted_post_groups))
print("Info: Data sent successfully to url: '{}'. Response is {}"
      .format, request_ip, response)
