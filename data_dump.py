import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
Database_name = "aps"
collection_name = "sensor"
data_file_path = '/config/workspace/aps_failure_training_set1.csv'


if __name__ == '__main__':
    df = pd.read_csv(data_file_path)
    print(df.shape)


# Convert dataframe into json so that we can dump the record in mongo db
df.reset_index(drop=True, inplace=True)
json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])

#Insert the converted json data into mongodb
client[Database_name][collection_name].insert_many(json_record)