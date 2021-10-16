# Курс 2. Курсовая. свой Instagram с едой, котами и еще раз едой!

from flask import Flask, request, render_template, redirect
from funcs import *

app = Flask(__name__)


@app.route('/')
def main_page():
    posts = get_posts()
    bookmarks = get_bookmarks()
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@app.route('/posts/<int:post_id>/')
def post_page(post_id):
    if post_id:
        post = get_one_post(post_id)
        if post:
            bookmarks = get_bookmarks()
            return render_template('post.html', post=post, bookmarks=bookmarks)
    return 'Not found', 404


@app.route('/search/')
def search_page():
    search_txt = request.args.get('s')
    posts_found = []
    posts_max = 10 # Максимальное количество найденных постов на странице
    bookmarks = get_bookmarks()
    if search_txt:
        posts = get_posts()
        for post in posts:
            if search_txt.lower() in post['content'].lower():
                posts_found.append(post)
                if len(posts_found) == posts_max:
                    break
    else:
        search_txt = ''
    return render_template('search.html', posts=posts_found, search_txt=search_txt, bookmarks=bookmarks)


@app.route('/users/<username>/')
def user_page(username):
    posts = get_posts()
    bookmarks = get_bookmarks()
    posts_list = []
    for post in posts:
        if post['poster_name'] == username:
            posts_list.append(post)
    if posts_list:
        return render_template('user-feed.html', posts=posts_list, bookmarks=bookmarks)
    return 'Not found', 404


@app.route('/tag/<tagname>/')
def tag_page(tagname):
    posts = get_posts()
    bookmarks = get_bookmarks()
    posts_list = []
    for post in posts:
        if ('#' + tagname + ' ') in post['content']:
            posts_list.append(post)
    if posts_list:
        return render_template('tag.html', posts=posts_list, bookmarks=bookmarks)
    return 'Not found', 404


@app.route('/bookmarks/add/<int:post_id>/')
def add_bookmark(post_id):
    with open('data/bookmarks.json', encoding="utf-8") as f:
        bookmarks = json.load(f)
    bookmarks.append(post_id)
    with open('data/bookmarks.json', 'w', encoding="utf-8") as f:
        json.dump(bookmarks, f)
    return redirect('/', code=302)


@app.route('/bookmarks/remove/<int:post_id>/')
def del_bookmark(post_id):
    with open('data/bookmarks.json', encoding="utf-8") as f:
        bookmarks = json.load(f)
    bookmarks.remove(post_id)
    with open('data/bookmarks.json', 'w', encoding="utf-8") as f:
        json.dump(bookmarks, f)
    return redirect('/', code=302)


@app.route('/bookmarks/')
def bookmark_page():
    posts = get_posts()
    bookmarks = get_bookmarks()
    posts_list = []
    for post in posts:
        if post['pk'] in bookmarks:
            posts_list.append(post)
    if posts_list:
        return render_template('bookmarks.html', posts=posts_list)
    return 'Not found', 404


if __name__ == '__main__':
    app.run(debug=True)
