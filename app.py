from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'New York, NY',
        'salary': '$120,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, CA',
        'salary': '$130,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Austin, TX',
        'salary': '$110,000'
    },
    {
        'id': 4,
        'title': 'UX Designer',
        'location': 'Bengaluru, India',
        'salary': '₹1,200,000'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def show_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)