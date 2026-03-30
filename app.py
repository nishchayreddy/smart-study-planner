from flask import Flask, render_template, request
from planner import generate_plan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    subjects = request.form.getlist('subject')
    days = request.form.getlist('days')
    difficulty = request.form.getlist('difficulty')

    plan = generate_plan(subjects, days, difficulty)

    return render_template('result.html', plan=plan)

if __name__ == '__main__':
    app.run(debug=True)