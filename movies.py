from flask import Flask, render_template
app = Flask(__name__)

movies = [
    {
        'title' : 'Whiplash',
        'director' : 'Damien Chazelle',
    },
    {
        'title' : 'Lord of the Rings',
        'director' : 'Peter Jackson'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', movies=movies)

@app.route("/movie")
def movie():
    return render_template('movie.html', title='Particular movie')

if __name__ == '__main__':
    app.run(debug=True)
