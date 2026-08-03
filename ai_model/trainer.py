import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier


class AITrainer:
    """
    Обучение моделей AI Trading Bot

    Первая версия:
    - XGBoost классификатор
    - обучение на исторических данных
    - оценка качества
    - сохранение модели
    """

    def __init__(self, model_path="ai_model/models"):

        self.model_path = model_path

        if not os.path.exists(self.model_path):
            os.makedirs(self.model_path)


    def prepare_data(self, df, target):

        X = df.drop(columns=[target])

        y = df[target]


        return train_test_split(
            X,
            y,
            test_size=0.2,
            shuffle=False
        )


    def train_xgboost(self, X_train, y_train):

        model = XGBClassifier(

            n_estimators=200,

            learning_rate=0.05,

            max_depth=5,

            random_state=42

        )


        model.fit(
            X_train,
            y_train
        )


        return model



    def evaluate(self, model, X_test, y_test):

        prediction = model.predict(X_test)


        accuracy = accuracy_score(
            y_test,
            prediction
        )


        return round(
            accuracy * 100,
            2
        )



    def save(self, model, name="xgboost_v1"):

        path = (
            f"{self.model_path}/{name}.pkl"
        )


        with open(path, "wb") as file:

            pickle.dump(
                model,
                file
            )


        return path