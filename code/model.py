from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

class CropRecommendationModel:
    def _init_(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, csv_file):
        data = pd.read_csv(csv_file)

        X = data[["temperature", "humidity", "soil_moisture"]]
        y = data["pump_status"]

        self.model.fit(X, y)
        joblib.dump(self.model, "crop_model.pkl")
        print("Model trained successfully!")

    def predict(self, temperature, humidity, soil_moisture):
        prediction = self.model.predict([[temperature, humidity, soil_moisture]])
        return prediction[0]
