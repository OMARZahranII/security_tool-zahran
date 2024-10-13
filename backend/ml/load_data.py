import pandas as pd

def load_vulnerability_data(filepath):
    df = pd.read_csv(filepath)
    X = df[['open_ports', 'services_running', 'configurations', 'cloud_provider']]
    y = df['vulnerability_found']
    return X, y
