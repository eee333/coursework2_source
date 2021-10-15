# All function for project

import json


def get_posts():
    with open('data/data.json', encoding="utf-8") as f:
        posts = json.load(f)
        for post in posts:
            comment_count = len(get_comments(post['pk']))
            post['comment_count'] = comment_count
            post['content_short'] = comment_count
            if '#' in post['content']:
                post['content'] = make_hash(post['content'])
        return posts


def get_comments(post_id):
    comment_list = []
    with open('data/comments.json', encoding="utf-8") as f:
        comments = json.load(f)
    for comment in comments:
        if comment['post_id'] == post_id:
            comment_list.append(comment)
    return comment_list


def make_link(txt):
    link = f'<a href="/tag/{txt[1:]}">{txt}</a>'
    return link


def make_hash(content):
    words = content.split()
    words_new = []
    for word in words:
        if '#' in word:
            word = make_link(word)
        words_new.append(word)
    return ' '.join(words_new)

