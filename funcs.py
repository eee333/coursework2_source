# All function for project


def get_posts():
    with open('data/data.json', encoding="utf-8") as f:
        posts = json.load(f)
        return posts

