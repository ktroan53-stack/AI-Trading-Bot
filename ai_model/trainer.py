import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier



class AITrainer:


    def __init__(
        self,
        model_path="ai_model/models"
    ):

        self.model_path = model_path


        if not os.path.exists(
            self.model_path
        ):

            os.makedirs(
                self.model_path
            )



    def prepare_data(
        self,
        df
    ):


        X = df.drop(
            columns=["target"]
        )


        y = df["target"]


        # классы для XGBoost
        y = y.replace(
            {
                -1:0,
                0:1,
                1:2
            }
        )


        return train_test_split(

            X,

            y,

            test_size=0.2,

            shuffle=False

        )



    def train_xgboost(
        self,
        X_train,
        y_train
    ):


        model = XGBClassifier(

            n_estimators=500,

            learning_rate=0.03,

            max_depth=6,

            subsample=0.8,

            colsample_bytree=0.8,

            objective="multi:softprob",

            num_class=3,

            eval_metric="mlogloss",

            random_state=42

        )


        model.fit(

            X_train,

            y_train

        )


        return model



    def evaluate(
        self,
        model,
        X_test,
        y_test
    ):


        prediction = model.predict(
            X_test
        )


        accuracy = accuracy_score(

            y_test,

            prediction

        )


        print(
            classification_report(
                y_test,
                prediction
            )
        )


        return round(
            accuracy * 100,
            2
        )



    def save(
        self,
        model,
        name="xgboost_v4"
    ):


        path = (

            f"{self.model_path}/"
            f"{name}.pkl"

        )


        with open(
            path,
            "wb"
        ) as file:

            pickle.dump(
                model,
                file
            )


        return path