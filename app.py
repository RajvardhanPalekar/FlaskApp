from flask import Flask, render_template, url_for
app = Flask(__name__)

groups = [
    {
        'name': 'Avengers Family',
        'admin': 'Tony Stark',
        'participants': 6
    },
    {
        'name': 'Workout Buddies',
        'admin': 'Bruce Banner',
        'participants': 5
    },
    {
        'name': 'Work Friends',
        'admin': 'Steve Rogers',
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

if __name__ == '__main__':
    app.run(debug=True)