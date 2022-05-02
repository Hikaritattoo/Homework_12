import json

POST_PATH = 'posts.json'


def load_posts():
    with open(POST_PATH, 'r', encoding='UTF8') as file:
        posts = json.load(file)
    return posts


def upload_posts(posts):
    with open(POST_PATH, 'w', encoding='UTF8') as file:
        json.dump(posts, file, indent=4)


