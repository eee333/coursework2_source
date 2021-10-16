# Курс 2. Курсовая. свой Instagram с едой, котами и еще раз едой!

from flask import Flask, request, render_template
from funcs import *

app = Flask(__name__)


@app.route('/')
def main_page():
    posts = get_posts()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>/')
def post_page(post_id):
    if post_id:
        post = get_one_post(post_id)
        if post:
            return render_template('post.html', post=post)
    return 'Not found', 404


@app.route('/search/')
def search_page():
    search_txt = request.args.get('s')
    posts_found = []
    posts_max = 10 # Максимальное количество найденных постов на странице
    if search_txt:
        posts = get_posts()
        for post in posts:
            if search_txt.lower() in post['content'].lower():
                posts_found.append(post)
                if len(posts_found) == posts_max:
                    break
    else:
        search_txt = ''
    return render_template('search.html', posts=posts_found, search_txt=search_txt)


@app.route('/users/<username>/')
def user_page(username):
    posts = get_posts()
    posts_list = []
    for post in posts:
        if post['poster_name'] == username:
            posts_list.append(post)
    if posts_list:
        return render_template('user-feed.html', posts=posts_list)
    return 'Not found', 404


if __name__ == '__main__':
    app.run(debug=True)


