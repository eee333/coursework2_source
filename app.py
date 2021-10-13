# Курс 2. Курсовая. свой Instagram с едой, котами и еще раз едой!

from flask import Flask, request, render_template
from funcs import *

app = Flask(__name__)


@app.route('/')
def main_page():
    posts = get_posts()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)


