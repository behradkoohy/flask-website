from flask import Flask, render_template;

app = Flask(__name__)

posts = [
    {
        "author":"Behrad Koohy",
        "title":"The First Blog Post",
        "content":"This is huge, Behrad is actually doing something",
        "date":"4 June 2019"
    },
    {
        "author":"Hashem Koohy",
        "title":"The Second Blog Post",
        "content":"No he's not",
        "date":"4 June 2019"
    }
]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return "<h1>about page"