import pickle
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))

cols = ['age', 'sex', 'children', 'smoker', 'region', 'grade']

# value = [18, 'female', 4, 'no', 'northeast', 'obesity']


def predict(list_values=None):
    to_predict = dict(zip(cols, list_values))
    to_predict = pd.DataFrame(to_predict, index=[0])
    return model.predict(to_predict)[0]