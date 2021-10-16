# All function for project

import json


def get_posts():
    with open('data/data.json', encoding="utf-8") as f:
        posts = json.load(f)
        for post in posts:
            comment_count = len(get_comments(post['pk']))
            post['comment_count'] = comment_count
            post['content_short'] = cut_comment(post['content'])
            if '#' in post['content_short']:
                post['content_short'] = make_hash(post['content_short'])
        return posts


def get_one_post(post_id):
    with open('data/data.json', encoding="utf-8") as f:
        posts = json.load(f)
    for post in posts:
        if post['pk'] == post_id:
            if '#' in post['content']:
                post['content'] = make_hash(post['content'])
            comment_list = get_comments(post_id)
            post['comments'] = comment_list
            return post
    return False


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


def cut_comment(txt):
    symbols = ',.!?: '
    comment_short = txt[:50]
    if txt[:51] not in symbols:
        comment_short = comment_short[:comment_short.rfind(' ')]
    return comment_short

