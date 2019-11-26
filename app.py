from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = "d2f5cc0afca8ffb79e5cdc7a39181329"

groups = [
    {
        'name': 'Avengers Family',
        'admin': 'starkTony3000',
        'participants': 6
    },
    {
        'name': 'Workout Buddies',
        'admin': 'angryBanner1',
        'participants': 5
    },
    {
        'name': 'Work Friends',
        'admin': 'captain$Rogers',
        'participants': 10
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', groups=groups)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Hello {form.username.data}, Welcome to FlaskApp!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@flaskapp.com' and  form.password.data == 'password':
            flash(f'Welcome back admin!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Invalid email or password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)