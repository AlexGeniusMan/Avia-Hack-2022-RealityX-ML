import json
import os
import pandas as pd
import numpy as np

from catboost import CatBoostRegressor

from app.Encoder import Encoder


TARGETS = {}
with open("app/targets.json", "r") as fp:
    TARGETS = json.load(fp)


def dataframe_to_dict(dataframe: pd.DataFrame):
    result = []
    dataframe = dataframe.reset_index()
    for index, row in dataframe.iterrows():
        asd = {}
        row = row.drop(labels=['index'])
        asd['engine_id'] = row['engine_id']
        asd['flight_phase'] = row['flight_phase']
        asd['flight_datetime'] = row['flight_datetime']
        metrics = {}
        row = row.drop(labels=['engine_id', 'flight_datetime', 'flight_phase'])
        for label in row.keys():
            metrics[label] = None if np.isnan(row[label]) else row[label]
        asd['metrics'] = metrics
        result.append(asd)
    return result


def generate_val_part(key: str, x: pd.DataFrame, aircraft_grp_encoder, empty:list = None):
    engine_type, flight_phase = key.split(' ')
    x = x[x['engine_type'] == engine_type]
    x = x[x['flight_phase'] == flight_phase]
    if(empty is None):
        empty = []
        size = x.shape[0]
        for column in x.drop(columns=['engine_type', 'flight_phase']).columns:
            if (x[column].isna().sum() / size) > 0.7:
                empty.append(column)
    x = x.drop(columns=empty)
    x['aircraft_grp'] = x['aircraft_grp'].apply(aircraft_grp_encoder.encode_single)
    x = x.fillna(-100)
    return x[['engine_id', 'flight_datetime', 'flight_phase']], x.drop(columns=['engine_id', 'aircraft_id', 'flight_datetime', 'engine_family', 'engine_type', 'manufacturer', 'ac_manufacturer', 'aircraft_type', 'aircraft_family', 'flight_phase']), empty


def make_prediction(filepath: str, model_dir: str = "app/models"):
    x_val = pd.read_csv(filepath)
    x = pd.read_csv('app/X_train.csv')
    x['engine_type'] = x['engine_type'].map(lambda x: x.replace('/', '_'))
    x = x.astype({'n1_modifier': 'int32'})
    aircraft_grp_encoder = Encoder(x['aircraft_grp'].unique())
    result = None
    for key, metrics in TARGETS.items():
        df = None
        for metric in metrics:
            _, _, empty = generate_val_part(key, x, aircraft_grp_encoder)
            ids, x_val_part, _ = generate_val_part(key, x_val, aircraft_grp_encoder, empty)
            if x_val_part.shape[0] == 0:
                continue
            model = CatBoostRegressor().load_model(os.path.join(model_dir, key, f'{metric}.cbm'))
            prediction = model.predict(x_val_part)
            ids[metric] = list(prediction)
            if df is None:
                df = ids
            else:
                df = pd.merge(df, ids, on=['engine_id', 'flight_datetime', 'flight_phase'], how='outer')
        if result is None:
            result = df
        else:
            result = pd.concat((result, df))
    return dataframe_to_dict(result)
