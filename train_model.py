import pandas as pd
from pycaret.classification import setup, create_model, save_model

# Load dataset
data = pd.read_csv('phishing_dataset.csv')

# Clean column names (just in case)
data.columns = data.columns.str.strip()

# Set up PyCaret (silent removed)
clf = setup(data=data, target='is_phishing', session_id=42, html=False, fold=2)

# Train the model
model = create_model('rf')

# Save the model
save_model(model, 'phishingdetection')
