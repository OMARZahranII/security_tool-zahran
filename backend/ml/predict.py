from backend.ml.threat_detection import train_advanced_model
from backend.ml.load_data import load_vulnerability_data

# Assuming you have a dataset path available
X, y = load_vulnerability_data('path/to/vulnerability_dataset.csv')
model = train_advanced_model(X, y)

def predict_vulnerability(scan_data):
    prediction = model.predict([scan_data])
    return bool(prediction[0])
