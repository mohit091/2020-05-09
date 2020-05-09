import pandas as pd
import json
import traceback



try:
    json_object = {"title": "Floor Access Event","type": "object","properties":"","required":""}
    json_list = []


    def read_source_data(file_path):
        df= pd.read_csv(file_path)
        return df

    def process_source_data():
        df=read_source_data('data.csv')
        required=list(df.columns.values)
        df = df.to_json(orient='records')
        property_object= json.loads(df)
        json_object['properties']=property_object
        for i in property_object:
            json_object['properties'] = i
            json_object['required'] = required
            json_list.append(json_object.copy())
        return json_list


    def processed_data_to_file(output_file_path):
        json_list=process_source_data()
        df=pd.DataFrame(json_list)
        df.to_json(output_file_path, orient='records', lines=True)




    if __name__ == "__main__":
        processed_data_to_file('data.json')


except:
    errMsg = traceback.format_exc()
    print (errMsg)



