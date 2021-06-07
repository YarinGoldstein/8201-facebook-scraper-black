from datetime import datetime
import facebook_scraper as scraper
import dateString

target_profile = {'id': "123456789", 'name': "shirly.dwek"}
cur_credentials = ("danielking1002@walla.com", "1101999d")

target_posts = [_ for _ in scraper.get_posts(
    target_profile['name'], credentials=cur_credentials, pages=1)]
formatted_posts = [{'text': curPost['post_text'],
                    'publish_date': curPost['time'],
                    'scrape_date': dateString.format(datetime.now())} for curPost in target_posts]
print("done")
