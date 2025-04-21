
# 🛡️ Phishing URL Detection Web App

This is a Flask-based web application that detects whether a given URL is **phishing** or **legitimate** using a machine learning model built with **PyCaret**.

---

## 🚀 Features

- ✅ User-friendly web interface
- 🔍 Input a URL and get instant prediction (Phishing or Legitimate)
- ⚙️ Backend powered by a PyCaret-trained machine learning model
- 🧠 Model uses a transformation pipeline to handle URL features

---

## 🧰 Tech Stack

- **Frontend:** HTML, CSS (via Flask templates)
- **Backend:** Python, Flask
- **Machine Learning:** PyCaret
- **Model Loading:** `joblib`

---


## ▶️ How to Run the Project

### 🔧 1. Install Dependencies

Make sure you have Python 3.7+ installed.

```bash
pip install -r requirements.txt
```

### ▶️ 2. Run the Flask App

```bash
python app.py
```

> Output:
```
Transformation Pipeline and Model Successfully Loaded
 * Running on http://127.0.0.1:5000/
```

Open your browser and go to `http://127.0.0.1:5000/`

---

## 🌐 Usage

1. Enter any URL into the input field.
2. Click the **Predict** button.
3. The app will display whether the URL is **Phishing** or **Legitimate** based on the model's output.

---

## ⚠️ Common Errors

### ❌ `KeyError: 'Score'`

This means you're trying to access a column that does not exist in the model output. Use `'Label'` instead of `'Score'` if your model returns a binary classification.

Update this line:

```python
prediction = result['Label'][0]
```

> Run `pip freeze > requirements.txt` to generate your own.

---

## 🧠 Model Training (Optional)

You can train a new model using PyCaret like this:

```python
from pycaret.classification import *
clf = setup(data, target='is_phishing')
best = compare_models()
save_model(best, 'phishing_model')
```

---

## 📃 License

This project is for educational/demo purposes. Use at your own discretion in production environments.

---

## ✨ Author

Created by [Shaik Dadapeer] 👨‍💻  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/shaik-dadu-7b5146297/) or [GitHub](https://github.com/dadu000)!
