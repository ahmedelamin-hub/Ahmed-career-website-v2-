from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Jeddah, Saudi Arabia',
        'salary': 'Sar. 10,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': "Mecaa, Saudi Arabia",
        
    },
    {
        'id': 3,
        'title': 'Front-End Developer',
        'location': 'Remote',
        'salary': 'Sar. 12,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                          jobs = JOBS)

@app.route("/api/jobs")
def jobs_list():
    return jsonify(JOBS)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)