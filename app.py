from flask import Flask, render_template, request
import pandas as pd
from pycaret.classification import load_model, predict_model
import featureExtractor

app = Flask(__name__)
model = load_model('phishingdetection')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form['url']
        input_df = pd.DataFrame([{'url': url}])
        
        result = predict_model(model, data=input_df)
        print(result)  # Debug: See what columns are there
        
        prediction = result['Label'][0]  # Use correct key
        return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)



# app.py

# from flask import Flask, render_template, request
# import pandas as pd
# from pycaret.classification import load_model
# import featureExtractor  # our custom feature extractor

# app = Flask(__name__)

# # Load PyCaret model
# model = load_model('phishingdetection')  # load PyCaret model

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     url = request.form['url']
#     features = featureExtractor.extract_features(url)
#     print(f"URL: {url}, Extracted features: {features}")  # Debug
#     df = pd.DataFrame([features], columns=['url_length', 'dot_count', 'slash_count', 'contains_https'])
#     prediction = model.predict(df)
#     print(f"Prediction: {prediction[0]}")  # Debug
#     return str(prediction[0])
# if __name__ == '__main__':
#     app.run(debug=True)

  
