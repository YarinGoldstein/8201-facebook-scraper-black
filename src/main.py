import facebook_scraper as scraper

target_profile = {'id': "123456789", 'name': "shirly.dwek"}
cur_credentials = ("danielking1002@walla.com", "1101999d")

target_posts = [_ for _ in scraper.get_posts(
    target_profile['name'], credentials=cur_credentials, pages=1)]
formatted_posts = [curPost for curPost in target_posts]
