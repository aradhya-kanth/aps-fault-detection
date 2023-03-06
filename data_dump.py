import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")
    df.reset_index(drop=True, inplace=True)
    json_records = list(json.loads(df.T.to_json()).values())

    client[DATABASE][COLLECTION_NAME].insert_many(json_records)
