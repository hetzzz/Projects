from flask import Flask, render_template, request
import pandas as pd
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from tensorflow.keras.models import load_model

df = pd.read_csv("sqliv2.csv",encoding='utf-16')
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer( min_df=2, max_df=0.7, max_features=4096, stop_words=stopwords.words('english'))
posts = vectorizer.fit_transform(df['Sentence'].values.astype('U')).toarray()

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def login():
    pass

@app.route("/predict", methods=['POST'])
def predict():
    query =  str(request.form['sqli_query'])

    model = load_model("ql_rl_model.h5")
    # model1.summary()
    print("model loaded")

    print(query)
    input_value = [query]

    input_value = vectorizer.transform(input_value).toarray()  
    input_value.shape = (1,64,64,1)    
    # result = model.predict(input_value)
    result = (model.predict(input_value) > 0.5).astype("int32")
    print(result)

    if (result>=0.5):        
        return render_template('index.html', query_result=f'SQL Injection Vulnerability -> DETECTED')
    else:
        return render_template('index.html', query_result=f'SQL Injection Vulnerability -> NOT DETECTED')

if __name__ == "__main__":
    app.run()
