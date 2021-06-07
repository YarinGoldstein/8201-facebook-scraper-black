from datetime import datetime
import base64
import requests
import facebook_scraper as scraper

target_profile = {'id': "123456789", 'name': "shirly.dwek"}
cur_credentials = ("danielking1002@walla.com", "1101999d")
date_format_string = "%Y-%m-%dT%H:%M:%S"

target_posts = scraper.get_posts(
    target_profile['name'], credentials=cur_credentials, pages=1)
formatted_posts = [{'text': curPost['post_text'],
                    'publish_date': (curPost['time'].strftime(date_format_string)
                                     if curPost['time'] is not None
                                     else None),
                    'scraping_date': datetime.now().strftime(date_format_string),
                    'image': base64.b64encode(requests.get("https://scontent.fhfa2-2.fna.fbcdn.net/v/t1.6435-1/195649319_102533148722302_1510341430419161353_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=7206a8&_nc_ohc=QfEEyhQ0S4kAX-QtXoO&tn=uimB07pEebhS63Nq&_nc_ht=scontent.fhfa2-2.fna&oh=44ee2902136aef6133b922522cd852e2&oe=60E37278").content)}
                   for curPost in target_posts]
print("done")
