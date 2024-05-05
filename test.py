import pandas as pd
import pickle


def load_model():
    with open('svm_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model    
    
def test_model():
    model = load_model()
    
    data = pd.DataFrame({
        'Overall_rating': [1,4],
        'work_life_balance': [1,4],
        'skill_development': [1,4],
        'salary_and_benefits': [1,4],
        'job_security': [1,4],
        'career_growth': [1,4],
        'work_satisfaction': [1,4]
    })
    
    assert model.predict(data) == ['Negative','Positive']