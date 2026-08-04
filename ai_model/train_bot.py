import sys
import os

# добавляем корень проекта в путь
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
    print("AI MODEL TRAINING START")
    print("==============================")


    df = pd.read_csv(
        "data/training_dataset.csv"
    )


    trainer = AITrainer()



    X_train, X_test, y_train, y_test = trainer.prepare_data(
        df,
        "target"
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
        "xgboost_v1"
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