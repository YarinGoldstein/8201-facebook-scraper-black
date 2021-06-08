import base64
import requests


def get_image_from_post_group(group):
    imageUrl = next((cur_post['image'] for cur_post in group
                     if (cur_post['text'] == ''
                         and cur_post['image'] != '')), None)
    return str(base64.b64encode(requests.get(imageUrl).content))[2:-1]
