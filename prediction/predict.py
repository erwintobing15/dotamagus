from recommendation.recommender import convert_heroes_name_to_id
from .preprocessing import preprocess

# from tensorflow import keras
import xgboost as xgb

def get_prediction(radiant_heroes, dire_heroes):

    radiant_heroes = convert_heroes_name_to_id(radiant_heroes)
    dire_heroes = convert_heroes_name_to_id(dire_heroes)

    input_data = preprocess(radiant_heroes,dire_heroes)
    input_data = input_data.to_numpy()

    # import model
    # model = keras.models.load_model("prediction/model.h5")
    model = xgb.XGBClassifier()
    model.load_model("prediction/model.txt")

    # run prediction
    predict_result = model.predict_proba(input_data)
    win_rate = int(predict_result[0][1] * 100)

    return win_rate
