# Курс 2. Курсовая. свой Instagram с едой, котами и еще раз едой!

from flask import Flask, request, render_template
from funcs import *

app = Flask(__name__)


@app.route('/')
def main_page():
    posts = get_posts()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>/')
def post_page(postid):
    posts = get_posts()
    for post in posts:
        if postid == post['pk']:
            return render_template('post.html', post=post)
    return 'Not found', 404


if __name__ == '__main__':
    app.run(debug=True)


