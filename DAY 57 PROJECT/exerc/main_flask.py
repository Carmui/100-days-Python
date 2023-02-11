from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_req = requests.get(gender_url)
    gender_data = gender_req.json()
    gender_api = gender_data["gender"]

    age_url = f"https://api.agify.io/?name={name}"
    age_req = requests.get(age_url)
    age_data = age_req.json()
    age_api = age_data["age"]

    return render_template('guess.html', name=name, gender=gender_api, age=age_api)


@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/6df4a5661ab5cf357bf5"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)



