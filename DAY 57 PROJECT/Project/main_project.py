from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/6df4a5661ab5cf357bf5"
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def home():

    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    return render_template('post.html', id=blog_id, posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
