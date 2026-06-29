from model import CropRecommendationModel

def main():
    model = CropRecommendationModel()

    # Dataset path
    csv_file = "../dataset/crop_data.csv"

    # Train model
    model.train(csv_file)

    print("Training Completed Successfully!")

if _name_ == "_main_":
    main()
