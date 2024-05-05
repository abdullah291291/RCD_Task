from flask import Flask, render_template, request, redirect, url_for
import csv
import pickle
import pandas as pd

app = Flask(__name__)


def load_model():
    # Load the model from the file
    with open('svm_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def get_sentiment_prediction(data):
    model = load_model()
    return model.predict(data)    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_review', methods=['POST'])
def submit_review():
    overall_rating = int(request.form['overall_rating'])
    work_satisfaction = int(request.form['work_satisfaction'])
    career_growth = int(request.form['career_growth'])
    skill_development = int(request.form['skill_development'])
    salary_benefits = int(request.form['salary_benefits'])
    work_life_balance = int(request.form['work_life_balance'])
    job_secuirty = int(request.form['job_secuirty'])
    
    data = pd.DataFrame({
        'Overall_rating': [overall_rating],
        'work_life_balance': [work_life_balance],
        'skill_development': [skill_development],
        'salary_and_benefits': [salary_benefits],
        'job_security': [job_secuirty],
        'career_growth': [career_growth],
        'work_satisfaction': [work_satisfaction]
    })
    
    pred = get_sentiment_prediction(data)
    return render_template('index.html', prediction=pred[0])

if __name__ == '__main__':
    app.run(debug=True)
