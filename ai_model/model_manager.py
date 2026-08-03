import os
import pickle


class ModelManager:
    """
    Управление AI моделями
    AI Trading Bot

    Функции:
    - сохранение моделей
    - загрузка моделей
    - проверка существования моделей
    - управление версиями
    """

    def __init__(self, model_path="ai_model/models"):

        self.model_path = model_path

        if not os.path.exists(self.model_path):
            os.makedirs(self.model_path)


    def save_model(self, model, name):

        file_path = f"{self.model_path}/{name}.pkl"

        with open(file_path, "wb") as file:
            pickle.dump(model, file)

        return file_path


    def load_model(self, name):

        file_path = f"{self.model_path}/{name}.pkl"

        if not os.path.exists(file_path):
            return None

        with open(file_path, "rb") as file:
            model = pickle.load(file)

        return model


    def model_exists(self, name):

        file_path = f"{self.model_path}/{name}.pkl"

        return os.path.exists(file_path)


    def get_models(self):

        if not os.path.exists(self.model_path):
            return []

        return [
            file
            for file in os.listdir(self.model_path)
            if file.endswith(".pkl")
        ]