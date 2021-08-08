from recommendation.recommender import convert_heroes_name_to_id
from .preprocessing import preprocess

from tensorflow import keras

def get_prediction(radiant_heroes, dire_heroes):

    radiant_heroes = convert_heroes_name_to_id(radiant_heroes)
    dire_heroes = convert_heroes_name_to_id(dire_heroes)

    input_data = preprocess(radiant_heroes,dire_heroes)
    input_data = input_data.to_numpy()

    # import model
    model = keras.models.load_model("prediction/model.h5")

    # run prediction
    predict_result = model.predict(input_data)
    win_rate = int(predict_result[0][1] * 100)

    return win_rate
