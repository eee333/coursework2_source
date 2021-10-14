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
    posts = get_posts()
    for post in posts:
        if post_id == post['pk']:
            comment_list = get_comments(post_id)
            return render_template('post.html', post=post, comments=comment_list)
    return 'Not found', 404


@app.route('/search/')
def search_page():
    search_txt = request.args.get('s')
    posts_found = []
    if search_txt:
        posts = get_posts()
        for post in posts:
            if search_txt.lower() in post['content'].lower():
                posts_found.append(post)
    else:
        search_txt = ''
    return render_template('search.html', posts=posts_found, search_txt=search_txt)


if __name__ == '__main__':
    app.run(debug=True)


