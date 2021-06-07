from datetime import datetime
import facebook_scraper as scraper

target_profile = {'id': "123456789", 'name': "shirly.dwek"}
cur_credentials = ("danielking1002@walla.com", "1101999d")
date_format_string = "%Y-%m-%dT%H:%M:%S"

target_posts = [_ for _ in scraper.get_posts(
    target_profile['name'], credentials=cur_credentials, pages=1)]
formatted_posts = [{'text': curPost['post_text'],
                    'publish_date': (curPost['time'].strftime(date_format_string)
                                     if curPost['time'] is not None
                                     else None),
                    'scrape_date': datetime.now().strftime(date_format_string)}
                   for curPost in target_posts]
print("done")
