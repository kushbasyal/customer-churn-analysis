import pandas as pd
from config_paths import raw_data_path
print(f"Raw Data Path: {raw_data_path}")

def load_data (data_path):
    try:
        df = pd.read_csv(data_path)
        print("Data Load Sucessfully:")
        return df
    except FileNotFoundError:
        print("File Not Found")
        return None
    
if __name__ == "__main__":
    df = load_data(raw_data_path)
    print(df.head())