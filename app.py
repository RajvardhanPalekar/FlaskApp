from flask import Flask, render_template
app = Flask(__name__)

groups = [
    {
        'name': 'Marvel Family',
        'admin': 'Tony Stark',
        'participants': 8
    },
    {
        'name': 'Health Buddies',
        'admin': 'Bruce Banner',
        'participants': 3
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