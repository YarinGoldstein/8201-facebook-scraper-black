import facebook_scraper as scraper

cur_credentials = ("danielking1002@walla.com","1101999d")
target_profile_name = 'shirly.dwek'

target_posts = [_ for _ in scraper.get_posts(target_profile_name,credentials=cur_credentials, pages=1)]
print(target_posts)
# print(scraper.get_profile('daniel.rogel.58'))