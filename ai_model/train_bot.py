import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import pandas as pd

from ai_model.trainer import AITrainer



def main():

    print("==============================")
    print("AI MODEL TRAINING v4 START")
    print("==============================")


    # Загружаем большой датасет 2018-2026
    df = pd.read_csv(
        "data/training_dataset_v3.csv"
    )


    print(
        "DATASET ROWS:",
        len(df)
    )


    trainer = AITrainer()


    X_train, X_test, y_train, y_test = trainer.prepare_data(
        df
    )


    print(
        "TRAINING XGBOOST v4..."
    )


    model = trainer.train_xgboost(
        X_train,
        y_train
    )


    accuracy = trainer.evaluate(
        model,
        X_test,
        y_test
    )


    print(
        "MODEL ACCURACY:",
        accuracy,
        "%"
    )


    path = trainer.save(
        model,
        "xgboost_v4"
    )


    print(
        "MODEL SAVED:"
    )

    print(
        path
    )


    print("==============================")
    print("TRAINING COMPLETE")
    print("==============================")



if __name__ == "__main__":

    main()