from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '974ffa637177ef3fe7382d23f9fb0cb8d9529bc2803b6d72b10809349095e0ce'


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
    return render_template('about.html', title="About Page")


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Please check email and password', 'danger')
    return render_template('login.html', title="Log In", form=form)


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title="Register", form=form)
