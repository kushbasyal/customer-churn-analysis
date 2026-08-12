import os
import json


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# if its inside folder congig then
# config_path = os.path.join(project_root, "config", "config.json")

config_path = os.path.join(project_root, "config.json")

with open (config_path, "r") as f:
    config = json.load(f)

raw_data_path = os.path.join(project_root, config["data"]["customer_churn_dataset"])

clean_customer_path = os.path.join(project_root, config["data"]["clean_customer_dataset"])

if __name__ == "__main__":
    print("project_root", project_root)
    print("Raw data", raw_data_path)
    print("Processed dtat", clean_customer_path)
